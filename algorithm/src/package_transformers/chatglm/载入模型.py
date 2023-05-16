from transformers import AutoTokenizer, AutoModel

pretrain_model_dir = '/opt/project/algorithm/src/pretrain_model/THUDM_chatglm-6b-int4'
tokenizer = AutoTokenizer.from_pretrained(pretrain_model_dir, trust_remote_code=True)
# model = AutoModel.from_pretrained(pretrain_model_dir, trust_remote_code=True).half().cuda()
model = AutoModel.from_pretrained(pretrain_model_dir, trust_remote_code=True).float()
model = model.eval()

# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)
# """
# 你好👋!我是人工智能助手 ChatGLM-6B,很高兴见到你,欢迎问我任何问题。
# """
# response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
# print(response)
# """
# 晚上睡不着可能会让你感到焦虑或不舒服,但以下是一些可以帮助你入睡的方法:
# 1. 制定规律的睡眠时间表:保持规律的睡眠时间表可以帮助你建立健康的睡眠习惯,使你更容易入睡。尽量在每天的相同时间上床,并在同一时间起床。
# 2. 创造一个舒适的睡眠环境:确保睡眠环境舒适,安静,黑暗且温度适宜。可以使用舒适的床上用品,并保持房间通风。
# 3. 放松身心:在睡前做些放松的活动,例如泡个热水澡,听些轻柔的音乐,阅读一些有趣的书籍等,有助于缓解紧张和焦虑,使你更容易入睡。
# 4. 避免饮用含有咖啡因的饮料:咖啡因是一种刺激性物质,会影响你的睡眠质量。尽量避免在睡前饮用含有咖啡因的饮料,例如咖啡,茶和可乐。
# 5. 避免在床上做与睡眠无关的事情:在床上做些与睡眠无关的事情,例如看电影,玩游戏或工作等,可能会干扰你的睡眠。
# 6. 尝试呼吸技巧:深呼吸是一种放松技巧,可以帮助你缓解紧张和焦虑,使你更容易入睡。试着慢慢吸气,保持几秒钟,然后缓慢呼气。
# 如果这些方法无法帮助你入睡,你可以考虑咨询医生或睡眠专家,寻求进一步的建议。
# """

while True:
    query = input('query:')
    response, history = model.chat(tokenizer, query, history=[])
    print(response)
