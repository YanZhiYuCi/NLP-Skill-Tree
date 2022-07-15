import torch
from torch.nn.modules import Linear

input_dim = 4096
output_dim = 2
num_prompt = 100
fine_tune_layer = Linear(in_features=input_dim, out_features=output_dim)
fine_tune_layer_1 = Linear(in_features=input_dim, out_features=output_dim)
optimizer = torch.optim.Adam(fine_tune_layer.parameters(), lr=1)
optimizer = torch.optim.Adam(
    [{'params': fine_tune_layer.parameters()}, {'params': fine_tune_layer_1.parameters(), 'lr': 1e-3}], lr=1e-2, )

temp = fine_tune_layer.parameters()
print('temp:', temp)
temp_tuple = (fine_tune_layer, fine_tune_layer_1)
temp = {1: fine_tune_layer, 2: fine_tune_layer_1}
torch.save(temp, 'embedding.pth')

temp_1 = torch.load('embedding.pth')
# c2 = torch.load('embedding.pth', map_location=torch.device('cpu'))
fine_tune_layer_load = temp_1[1]
fine_tune_layer_load_1 = temp_1[2]
