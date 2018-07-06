## 公用目录common

#### 系统配置文件
    <!-- 在yii2admin的根目录 -->
    .env 
    <!-- 内含数据库连接配置 -->

#### 公共配置
    common/config/*

#### 公共别名
    common/config/bootstrap.php
    <!-- 使用Yii::getAlias('@base')访问 -->

#### 公共模型
    common/models/*
    <!-- 继承 common/modelsgii 对应模型 -->

#### 公共的核心基类
    common/core/*
    <!-- 所有表单模型都继承 common\core\BaseModel -->
    <!-- 模型统一继承common\core\BaseActiveRecord -->
    <!-- 所有控制器都继承 common\core\Controller -->

#### gii生成的模型
    common/modelsgii/*

#### 自定义助手函数
    common/helpers/*

#### 多语言配置及应用
    common/config/main.php中的i18n
        sourceLanguage: 源语言,写在代码中的语言
        language: 目标语言,向最终用户显示内容的语,信息翻译服务主要是将文本消息从原语言翻译到目标语言
        'basePath'=>'@common/messages': 语言文件目录
        fileMap: 分类(category)名称映射的文件
    翻译:
        动态改变目标语言
        \Yii::$app->language = 'zh-CN';
        执行翻译
        echo \Yii::t('app', 'This is a string to translate!');
    开发及应用场景:
        - 假设源语言为繁体,则配置sourceLanguage/language为zh-TW
        - 用户切换语言,修改 \Yii::$app->language的值,并重新加载
        - 开发在代码中涉及到文字信息输出时全部用繁体,示例如:
            \Yii::t('backend', '這是一句繁體字信息的輸出');
        - 代码完成后,使用控制台命令message生成待翻译文件
            1. php yii message/config mymesconfig.php
            2. vim mymesconfig.php 编辑配置文件
            3. 修改sourcePath为要读取php文件的路径(@base)
            4. 修改messagePath为 i18n 的 basePath(@common/messages)
            5. 修改languages为应该被翻译成什么语言的一个数组(['zh-CN','en-US'])
            6. php yii message mymesconfig.php 生成待翻译文件
            7. 则文件common/messages/en-US/backend.php 可以看到...'這是一句繁體字信息的輸出' => '',待翻译