# GUI TOOL



## Getting Started



### essential（R：右边栏，L：左边栏 ，C：中间栏）

- [ ] R·打开文件:

  - 注意，这里文件可能不止一个（.csv/.json）【可以做两个图标，或者在弹出的对话框中各自选择】

  - 命令如下:

    ```
    wget https://bmbl.bmi.osumc.edu/downloadFiles/RESEPT/RESEPT.zip 
    unzip RESEPT.zip
    python evaluation_pipeline.py -expression S13/S13_filtered_feature_bc_matrix.h5  -meta S13/spatial/tissue_positions_list.csv  -scaler S13/spatial/scalefactors_json.json -output Demo_result  -embedding scGNN  -transform logcpm -label S13/S13_annotation.csv -model model_S13/S13_scGNN.pth
    ```

- [ ] R·保存文件：

  - 默认.png
  - 路径【未定】
  - Ctrl+s 快捷键
  - 图标：卡（Save）【原图就不错】

- [ ] R·运行/暂停

  - 如果无法实现暂停，就改为终止（强制）。
  - 运行和停止时，按键图标不同

- [ ] R·【未定，预留】

- [ ] R·放大

  - 这里考虑是按下按钮直接在中心点放大
  - 还是光标变成放大状态

- [ ] R·缩放比例

- [ ] R·缩小

- [ ] R·返回

  - 回到主界面（方便完成其他功能）

- [ ] R·帮助：跳转到相关网页【最好有一个】



- [ ] C·图像：

  - 进度条（多进程处理）

  

- [ ] L·参数：
  - 按钮，bar
    - 【细节有待推敲】
  - 选择、填空
    - 【同上】
- [ ] L·历史状态：
  - 【怎么实现还未知，需要保存的不仅是图片，还有参数的信息】

