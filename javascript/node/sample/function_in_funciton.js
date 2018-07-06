
// 函数内可以写函数

function fa(){
    console.info('in function: fa');
    fa1();
    fa2();
    function fa1(){
        console.info('  in function: fa1');
        fa1I();
        function fa1I(){
            console.info('      in function: fa1I');
        }
    }
    function fa2(){
        console.info("  in function: fa2");
    }
}

fa();