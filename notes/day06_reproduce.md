# Day06 克隆复现记录

## 一、复现目标

验证项目在新的目录和新的 Python 虚拟环境中，
能够按照 README 独立安装、测试和运行。

## 二、复现环境

- 操作系统：Windows 11
- Python版本：待填写
- PyCharm版本：待填写
- 复现日期：待填写

## 三、克隆命令

```bash
git clone --branch day06-jsonl-dataset --single-branch https://github.com/xl819436-creator/40day-lab.git 40day-lab-day06-check
```

## 四、创建环境

```bash
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 五、运行命令

```bash
.venv\Scripts\python.exe -m pytest day06/test_jsonl_io.py -v
.venv\Scripts\python.exe day06/jsonl_io.py
```

## 六、遇到的报错

待复现后填写。

## 七、最终输出

待复现后填写。

## 八、验收结果

- [ ] 成功克隆到第二个目录
- [ ] 成功创建全新虚拟环境
- [ ] 成功安装 requirements.txt
- [ ] 5项自动测试通过
- [ ] 成功读取10条 JSONL 数据
- [ ] 中文没有乱码
- [ ] 没有引用原项目绝对路径