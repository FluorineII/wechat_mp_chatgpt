# 使用说明
> 只是一个平平无奇的简介，适合没有钱买服务器，但是又想装逼玩chatgpt的人
## 前期准备
1. 拥有一个微信公众号
2. 注册华为云账号，开通functionGraph功能（每月前100万次调用免费）
3. 华为云花9块钱购买域名，用以映射functionGraph（微信公众号必须对外域名）

## 部署流程
### 一、华为云函数服务开通
1. 打开链接，根据提示操作
 > https://console.huaweicloud.com/functiongraph

2. 创建函数**testGPT**，如图所示，地区选择新加坡，运行时选择python3.9
![screenshot-20230328-203646.png](img%2Fscreenshot-20230328-203646.png)
### 二、代码处理
1. 下载代码，修改代码config配置
```
{
  "api_key": "**", // chatgpt的apikey
  "model": "gpt-3.5-turbo", // 对话模型
  "conversation_max_tokens": 1000, // 最长上下文
  "character_desc": "你是ChatGPT, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。",
  "token": "**", // 微信公众号的token
  "encoding_aes_key": "**", // 微信公众号的加密串
  "app_id": "**" // 微信公众号的appid
}
```

2. 在目录下运行 sh build.sh
3. 将archive.zip上传至华为云functionGraph **testGPT**
4. 将dependency.zip上传至华为云依赖包管理
5. **testGPT**函数配置中选择依赖包
6. 点击创建触发器，创建api接口，得到函数的测试链接
>该链接可用于测试公众号，不可用于真实公众号，微信屏蔽了此类链接
![screenshot-20230328-205249.png](img%2Fscreenshot-20230328-205249.png)
此时即可完成函数配置，部署函数之后，会生成接口已经可用
可以在微信公众号测试平台测试使用测试函数测试
>https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/index

在测试公众号发送消息，可以收到chatgpt回复
![20230328-210348.jpeg](img%2F20230328-210348.jpeg)
## 三、创建域名映射（如只需要在测试公众号玩耍，可以不需要此步骤）
1. 购买华为云域名，选择.top域名即可，9元/年
2. 在apig触发器页绑定自定义域名
![screenshot-20230328-205801.png](img%2Fscreenshot-20230328-205801.png)
## 四、配置微信公众号链接
选择明文模式，密文模式暂时不可用，mac的解密包在华为云服务器不可用
![img.png](img%2Fimg.png)