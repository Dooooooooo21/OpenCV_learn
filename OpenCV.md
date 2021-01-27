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

3. 优化技术

   - 避免使用循环
   - 尽量使用向量，numpy、openCV对向量进行了优化
   - ==利用高速缓存一致性==
   - 避免复制数组，使用视图代替复制



### PART 4

#### 图像处理

1. 颜色空间转换

   - BGR到灰度图、HSV等

   - `cvtColor(img, flag)` flag是转换类型

     - COLOR_BGR2GRAY
     - COLOR_BGR2HSV

     ```python
     flags = [i for i in dir(cv2) if str(i).startswith('COLOR_')]
     ```

2. 物体跟踪

   - 转换到HSV，选择颜色阈值，进行跟踪

   

