import argparse
import os

import torch
from torch.optim import AdamW
from torch.utils.data import DataLoader
from peft import (
    get_peft_config,
    get_peft_model,
    get_peft_model_state_dict,
    set_peft_model_state_dict,
    LoraConfig,
    PeftType,
    PrefixTuningConfig,
    PromptEncoderConfig,
)

import evaluate
from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer, get_linear_schedule_with_warmup, set_seed
from tqdm import tqdm

batch_size = 32
model_name_or_path = "roberta-large"
model_name_or_path = r"D:\Projects\machaoyangNLP\algorithm\src\package_transformers\RLHF\data\roberta-base-finetuned-jd-binary-chinese"
task = "mrpc"
peft_type = PeftType.LORA
# device = "cuda"
device = 'cpu'
num_epochs = 20

peft_config = LoraConfig(task_type="SEQ_CLS", inference_mode=False, r=8, lora_alpha=16, lora_dropout=0.1)
lr = 3e-4

if any(k in model_name_or_path for k in ("gpt", "opt", "bloom")):
    padding_side = "left"
else:
    padding_side = "right"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, padding_side=padding_side)
if getattr(tokenizer, "pad_token_id") is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

datasets = load_dataset("glue", task)
metric = evaluate.load("glue", task)


def tokenize_function(examples):
    # max_length=None => use the model max length (it's actually the default)
    outputs = tokenizer(examples["sentence1"], examples["sentence2"], truncation=True, max_length=None)
    return outputs


tokenized_datasets = datasets.map(
    tokenize_function,
    batched=True,
    remove_columns=["idx", "sentence1", "sentence2"],
)

# We also rename the 'label' column to 'labels' which is the expected name for labels by the models of the
# transformers library
tokenized_datasets = tokenized_datasets.rename_column("label", "labels")


def collate_fn(examples):
    return tokenizer.pad(examples, padding="longest", return_tensors="pt")


# Instantiate dataloaders.
train_dataloader = DataLoader(tokenized_datasets["train"], shuffle=True, collate_fn=collate_fn, batch_size=batch_size)
eval_dataloader = DataLoader(tokenized_datasets["validation"], shuffle=False, collate_fn=collate_fn, batch_size=batch_size)

model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path, return_dict=True)
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()

optimizer = AdamW(params=model.parameters(), lr=lr)

# Instantiate scheduler
lr_scheduler = get_linear_schedule_with_warmup(
    optimizer=optimizer,
    num_warmup_steps=0.06 * (len(train_dataloader) * num_epochs),
    num_training_steps=(len(train_dataloader) * num_epochs),
)

model.to(device)
for epoch in range(num_epochs):
    model.train()
    for step, batch in enumerate(tqdm(train_dataloader)):
        batch.to(device)
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()

    model.eval()
    for step, batch in enumerate(tqdm(eval_dataloader)):
        batch.to(device)
        with torch.no_grad():
            outputs = model(**batch)
        predictions = outputs.logits.argmax(dim=-1)
        predictions, references = predictions, batch["labels"]
        metric.add_batch(predictions=predictions, references=references)

    eval_metric = metric.compute()
    print(f"epoch {epoch}:", eval_metric)

# model.push_to_hub("smangrul/roberta-large-peft-lora", use_auth_token=True)

# import torch
# from peft import PeftModel, PeftConfig
# from transformers import AutoModelForCausalLM, AutoTokenizer
#
# peft_model_id = "smangrul/roberta-large-peft-lora"
# config = PeftConfig.from_pretrained(peft_model_id)
# inference_model = AutoModelForSequenceClassification.from_pretrained(config.base_model_name_or_path)
# tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
#
# # Load the Lora model
# inference_model = PeftModel.from_pretrained(inference_model, peft_model_id)
#
# inference_model.to(device)
# inference_model.eval()
# for step, batch in enumerate(tqdm(eval_dataloader)):
#     batch.to(device)
#     with torch.no_grad():
#         outputs = inference_model(**batch)
#     predictions = outputs.logits.argmax(dim=-1)
#     predictions, references = predictions, batch["labels"]
#     metric.add_batch(
#         predictions=predictions,
#         references=references,
#     )
#
# eval_metric = metric.compute()
# print(eval_metric)