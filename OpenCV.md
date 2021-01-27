### PART 3

#### 图像基础操作

1. 图像属性：行、列、通道、数据类型、像素数目

   ```python
   img = cv.imread(base_dir + '_DSC6981.JPG', 1)
   print(img.shape)
   # (3264, 4928, 3)
   
   # 像素数量
   print(img.size)
   # 48254976
   
   print(img.dtype)
   # uint8
   ```

2. ROI（region of interest），感兴趣区域

3. 拆分及合并通道

   ```python
   # split 耗时间
   b, g, r = cv.split(img)
   
   img = cv.merge((b, g, r))
   ```

4. 图像填充`copyMakeBorder()`



#### 图像上的算数运算

1. 图像加法`add()`
2. 图像混合`addWeighted()`
3. 位运算



#### 程序性能检测及优化

1. `getTickCount()`和`getTickFrequency()`

   ```python
   e1 = cv.getTickCount()
   # 执行代码
   e2 = cv.getTickCount()
   time = (e2 - e1) / cv.getTickFrequency()
   ```

2. 默认优化

   ```python
   # 检查是否启用了优化
   print(cv.useOptimized())
   
   # 关闭优化
   cv.setUseOptimized(False)
   ```

   

