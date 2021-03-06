## 单一职责原则
SRP,就一个类而言,应该仅有一个引起它变化的原因.

- 如果一个类承担的职责过多,就等于把这些职责耦合在一起,一个职责的变化可能会削弱或者抑制这个类完成其他职责的能力.
- 这种耦合会导致脆弱的设计,当变化发生时,设计会遭受到意想不到的破坏.
- 软件设计真正要做的许多内容,就是发现职责并把那些职责相互分离.
- 如果有多于一个的动机去改变一个类,那么这个类就具有多于一个的职责,就应该考虑类的职责分离.

### 方块游戏的设计
- 方块的可移动游戏区域,可以设计为一个二维整型数组用来表示坐标
- 方块的移动就是坐标上下标的变化
- 每个数组的值就是是否存在方块的标志,存在为1,不存在时缺省为0
- 消层就是[x,y]中循环x由0到9的数组值是否都等于1,并将其上方的数组值遍历下移一位
