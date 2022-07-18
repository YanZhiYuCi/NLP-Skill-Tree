# 一行代码写for循环和if else语句############################################################################################
all_labels = [1, 0, 1]
all_predicts = [1, 0, 0]
temp = [1 if per_label == per_pred else 0 for per_label, per_pred in zip(all_labels, all_predicts)]
print(temp)
