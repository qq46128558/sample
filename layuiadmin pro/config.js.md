# 全局配置文件

src/config.js：layuiAdmin 的全局配置文件，可随意修改

## 常用记录

### 是否开启未登入拦截
    interceptor: false

### Local Storage的Key名
    tableName: 'layuiAdmin'

### 自定义响应字段(API接口的返回json格式) 不建议改
~~~javascript
,response: {
      statusName: 'code' //数据状态的字段名称
      ,statusCode: {
        ok: 0 //数据状态一切正常的状态码
        ,logout: 1001 //登录状态失效的状态码
      }
      ,msgName: 'msg' //状态信息的字段名称
      ,dataName: 'data' //数据详情的字段名称
    }
~~~