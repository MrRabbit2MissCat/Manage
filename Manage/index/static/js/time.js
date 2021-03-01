 <!--删除数据-->
   function firm(id) {
        //利用对话框返回的值 （true 或者 false）
        if (confirm("你确定删除此条数据吗？")) {
            var my_id=id
            window.location="/del/?nid="+my_id;
            alert("成功删除");
        }
        else {
            alert("点击了取消");
        }

    }
    function success() {
        alert("成功上传");
    }
 <!--删除数据-->
   function firm_ware(id) {
        //利用对话框返回的值 （true 或者 false）
        if (confirm("你确定删除此条数据吗？")) {
            var my_id=id
            window.location="/del_ware/?nid="+my_id;
            alert("成功删除");
        }
        else {
            alert("点击了取消");
        }

    }

 <!--页面跳转-->
function pageClick(id) {
                var myid=id
                if(myid=="1")
                    this.location.href="/index/"
                else  if(myid=="2")
                    this.location.href="/show/"
                else  if(myid=="3")
                    this.location.href="/manage/"
                else  if(myid=="4")
                    this.location.href="/show_data/"
                else  if(myid=="5")
                    this.location.href="/treat/"
                else  if(myid=="7")
                    this.location.href="/warehouse/"
                else  if (confirm("你确定退出吗？")) {
                        var my_id=id
                        window.location="/login/";
                    }
                    else {
                        alert("点击了取消");
                    }
                        }

<!---实时时间-->
function auto(){
        var date=new Date();
        var Y=date.getFullYear();
        var M=date.getMonth()+1;
        var D=date.getDate();
        var H=date.getHours();
        var I=date.getMinutes();
        var S=date.getSeconds();
        document.getElementById('date').innerHTML=Y+'年'+M+'月'+D+'日'+"&nbsp;"+H+'时'+I+'分'+S+'秒';
        //设置定时器：每500秒自动调用自身一次
        setTimeout("auto()",500);
    }

function openLogin(my_id){
    document.getElementById("win").style.display="";
    document.getElementById("back").style.display="";

}
function closeLogin(){
   document.getElementById("win").style.display="none";
   document.getElementById("back").style.display="none";
}
<!---修改界面跳转-->
 function go_manage() {
    this.location.href="/manage/"

 }
 <!---修改界面跳转-->
 function go_warehouse() {
    this.location.href="/warehouse/"

 }