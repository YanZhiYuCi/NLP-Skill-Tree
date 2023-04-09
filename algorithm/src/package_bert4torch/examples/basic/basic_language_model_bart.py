# 测试bart语言模型的预测效果
# bert4torch需要转换一下权重，见convert文件夹中

# 选择v1还是v2
# file_dir = "F:/Projects/pretrain_ckpt/bart/[FudanNLP_torch_base]/"  # v1.0
file_dir = "F:/Projects/pretrain_ckpt/bart/[FudanNLP_torch_base_v2.0]/"  # v2.0


# ==============================transformers=====================================
from transformers import BertTokenizer, BartForConditionalGeneration
tokenizer = BertTokenizer.from_pretrained(f"{file_dir}")
model = BartForConditionalGeneration.from_pretrained(f"{file_dir}")

input_ids = tokenizer.encode("北京是[MASK]的首都", return_tensors='pt')
pred_ids = model.generate(input_ids, num_beams=4, max_length=20)
print('transformers output: ', tokenizer.convert_ids_to_tokens(pred_ids[0]))
# 输出： ['[SEP]', '[CLS]', '北', '京', '是', '中', '国', '的', '首', '都', '[SEP]'] 


# ==============================bert4torch=====================================
from bert4torch.models import build_transformer_model
from bert4torch.tokenizers import Tokenizer
from bert4torch.snippets import AutoRegressiveDecoder, Seq2SeqGeneration
import torch

# bert配置
config_path = f'{file_dir}/bert4torch_config.json'
checkpoint_path = f'{file_dir}/bert4torch_pytorch_model.bin'
dict_path = f'{file_dir}/vocab.txt'
device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = Tokenizer(dict_path, do_lower_case=True)
model = build_transformer_model(config_path, checkpoint_path, model='bart', segment_vocab_size=0).to(device)

# 第一种方式
class AutoTitle(AutoRegressiveDecoder):
    """seq2seq解码器
    """
    @AutoRegressiveDecoder.wraps(default_rtype='logits')
    def predict(self, inputs, output_ids, states):
        return model.decoder.predict([output_ids] + inputs)[-1][:, -1, :]  # 保留最后一位

    def generate(self, text, topk=4):
        token_ids, _ = tokenizer.encode(text, maxlen=128)
        token_ids = torch.tensor([token_ids], device=device)
        encoder_output = model.encoder.predict([token_ids])  # [encoder_hiddenstates, encoder_attention_mask]
        output_ids = self.beam_search(encoder_output, topk=topk)  # 基于beam search
        return tokenizer.decode(output_ids.cpu().numpy())

autotitle = AutoTitle(start_id=102, end_id=tokenizer._token_end_id, maxlen=32, device=device)

# 第二种方式
autotitle = Seq2SeqGeneration(model, tokenizer, start_id=102, end_id=tokenizer._token_end_id, mode='beam_search',
                              maxlen=32, default_rtype='logits', use_states=True)

print('bert4torch output: ', autotitle.generate("北京是[MASK]的首都", topk=4))