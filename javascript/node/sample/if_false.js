'use strict'

// '所有代表false的值'

if (undefined || null || 0 || -0 || NaN || "")
	console.info('true');
else
	console.info('false');
// false

console.info(null==undefined);
// true
