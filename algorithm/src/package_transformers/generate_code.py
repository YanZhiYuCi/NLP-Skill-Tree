from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("checkpoint/Salesforcecodegen-350M-multi")
model = AutoModelForCausalLM.from_pretrained("checkpoint/Salesforcecodegen-350M-multi")

# tokenizer = AutoTokenizer.from_pretrained("checkpoint/Salesforcecodegen-2B-multi")
# model = AutoModelForCausalLM.from_pretrained("checkpoint/Salesforcecodegen-2B-multi")

# text = "def hello_world():"
# input_ids = tokenizer(text, return_tensors="pt").input_ids
#
# generated_ids = model.generate(input_ids, max_length=128)
# print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))

# tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-multi")
# model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-multi")

# tokenizer = AutoTokenizer.from_pretrained("bigcode/santacoder")
# model = AutoModelForCausalLM.from_pretrained("bigcode/santacoder")

# tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-2B-multi")
# model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-2B-multi")

while True:
    # text = "def hello_world():"
    text = input("输入提示:")
    input_ids = tokenizer(text, return_tensors="pt").input_ids

    generated_ids = model.generate(input_ids, max_length=128)
    print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))