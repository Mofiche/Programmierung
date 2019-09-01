import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from torchvision import datasets, transforms
import torch.optim as optim
import os

kwargs = {'num_workers': 1, 'pin_memory': True}

train_data = torch.utils.data.DataLoader(datasets.MNIST('data', train=True, download=True,
                                                        transform=transforms.Compose([transforms.ToTensor(),
                                                                                      transforms.Normalize((0.1307,),
                                                                                                           (
                                                                                                               0.3081,))])),
                                         batch_size=128, shuffle=True, **kwargs)

test_data = torch.utils.data.DataLoader(datasets.MNIST('data', train=False,
                                                       transform=transforms.Compose([transforms.ToTensor(),
                                                                                     transforms.Normalize((0.1307,),
                                                                                                          (0.3081,))])),
                                        batch_size=128, shuffle=True, **kwargs)


class Netz(nn.Module):
    def __init__(self):
        super(Netz, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, kernel_size=4)
        self.conv2 = nn.Conv2d(20, 20, kernel_size=4)
        self.conv_dropout = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 180)
        self.fc2 = nn.Linear(180, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.max_pool2d(x, 2)
        x = F.relu(x)
        x = self.conv2(x)
        x = self.conv_dropout(x)
        x = F.max_pool2d(x, 2)
        x = F.relu(x)
        x = x.view(-1, 320)
        x = self.fc1(x)
        x = F.relu((x))
        x = self.fc2(x)
        return F.log_softmax(x)

    def num_flat_features(self, x):
        size = x.size()[1:]
        num = 1
        for i in size:
            num *= i
        return num


model = Netz()
model = model.cuda()

optimizer = optim.SGD(model.parameters(), lr=0.05, momentum=0.8)


def train(epoch):
    model.train()
    for batch_id, (data, target) in enumerate(train_data):
        data = data.cuda()
        target = target.cuda()
        data = Variable(data)
        target = Variable(target)
        optimizer.zero_grad()
        out = model(data)
        criterion = F.nll_loss
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()
        print('Epoche : {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(epoch, batch_id * len(data), len(train_data.dataset),
                                                                   100. * batch_id / len(train_data), loss.item()))


def test():
    model.eval()
    loss = 0
    correct = 0
    for (data, target) in test_data:
        data = Variable(data.cuda())
        target = Variable(target.cuda())
        out = model(data)
        loss += F.nll_loss(out, target, reduction='sum').item()
        prediction = out.data.max(1, keepdim=True)[1]
        correct += prediction.eq(target.data.view_as(prediction)).cpu().sum()
    loss = loss / len(test_data.dataset)
    print("Avg Loss :  {:.6f}".format(loss))
    print("Genauigkeit : {:.4f} %".format(100. * correct/len(test_data.dataset)))

if __name__ == '__main__':
    for epoch in range(1, 5):
        if os.path.isfile("mnist.pt"):
            model = torch.load("mnist.pt")
        train(epoch)
        torch.save(model, "mnist.pt")
    test()

