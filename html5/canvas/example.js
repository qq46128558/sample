var canvas=document.getElementById('canvas'),context=canvas.getContext('2d');

context.font='38pt Arial';
context.fillStyle="cornflowerblue";
context.fillText('Hello Canvas',canvas.width/2-150,canvas.height/2+15);
context.strokeStyle="blue";
context.strokeText('Hello Canvas',canvas.width/2-150,canvas.height/2+15);

// window坐标转canvas坐标
function windowsToCanvas(canvas,x,y){
	// 获取canvas元素的边界框(bounding box),该边界框的坐标是相对于整个窗口的
	var bbox=canvas.getBoundingClientRect();
	return {x:x-bbox.left*(canvas.width/bbox.width),
			y:y-bbox.top*(canvas.height/bbox.height)
	};
}