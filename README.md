# raspberrypi-recite-words

树莓派背单词小工具

![img](https://cdn.nlark.com/yuque/0/2020/png/2571709/1606025097177-ee77c16f-416f-45ca-8618-43f1bc71e148.png)

硬件安装博客：
https://www.yuque.com/zhongjiangtongzhi/estp1z/tqg8u6

## 开发环境构建

先安装 `python3`

然后安装函数库：

```bash
# 图像处理库
$pip install Pillow
# 数学函数库
$pip install numpy
# python控制树莓派GPIO的库
$pip install RPi.GPIO
# 驱动SPI接口的库（屏幕显示的通信接口）
$pip install spidev
```

## 运行调试

运行 `$ ptyhon init.py` 初始化词典数据库。

运行 `$ python main_dev.py` 在本机上预览运行效果



