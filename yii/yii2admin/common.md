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
    <!-- 所有表单模型都继承 common/core/BaseModel -->
    <!-- 模型统一继承common/core/BaseActiveRecord -->
    <!-- 所有控制器都继承 common/core/Controller -->

#### gii生成的模型
    common/modelsgii/*

#### 自定义助手函数
    common/helpers/*