from sklearn.metrics import classification_report

# 可以列表元素可以是整型也可以是字符串,support是标签的数量,不是预测的数量
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
print(classification_report(y_true=y_true, y_pred=y_pred))
print('=' * 80)
# labels可以有y_true和y_pred没有的
print(classification_report(y_true=y_true, y_pred=y_pred, labels=[0, 1, 2, 3]))
print('=' * 80)
# 指定target_names时需要先指定labels.并且两者元素需要对应
print(classification_report(y_true=y_true, y_pred=y_pred, labels=[0, 1, 2, 3], target_names=['北京', '上海', '成都', '南京']))
print('=' * 80)

# 以字符串为例
y_true = ['北京', '上海', '成都', '成都', '上海', '北京', '上海', '成都', '北京', '上海', '北京', '北京', '北京']
y_pred = ['北京', '上海', '成都', '上海', '成都', '成都', '上海', '成都', '北京', '上海', '北京', '北京', '北京']
print(classification_report(y_true, y_pred, labels=['北京', '上海', '成都']))
print('=' * 80)
print(classification_report(y_true, y_pred, labels=['北京', '上海', '成都', '南京']))
print('=' * 80)
print(classification_report(y_true, y_pred, labels=['北京', '上海', '成都'], target_names=['北京_北', '上海_上', '成都_成']))
