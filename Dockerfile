FROM python:3.9

# 安装依赖
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# 设置工作目录
WORKDIR /app
COPY . /app