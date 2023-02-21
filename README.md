## 组成
后端：python+fastapi 

前端：React+next.js

## 运行
前端通过yarn dev运行

后端通过uvicorn main:app --reload启动服务
如果是windows系统，需要注意前后端的运行问题
1. 前端可以在powershell里运行
2. 后端需要在cmd里运行，使用conda环境或别的。激活conda环境需要使用`call conda.bat activate`

## 所需组件
### 后端
1. pip install fastapi
2. pip install "uvicorn[standard]"
3. pip install fake-useragent
速度慢可以选择将pip配置为清华源`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`

### 前端
