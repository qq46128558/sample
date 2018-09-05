
#### 获取模块,控制器,动作ID
	// 注意是模块,不是模型(控制器与模型好像没有强关联?)
	Yii::$app->controller->module->id;
	Yii::$app->controller->id;
	Yii::$app->controller->action->id;
