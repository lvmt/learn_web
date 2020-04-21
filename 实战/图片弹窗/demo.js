
    $(function () { //页面加载完完成后，自动触发点击事件创造弹窗
        SetImage();
        document.getElementById("myImg").onclick(); //触发一次点击事件
    });

    function SetImage() {
        // 获取DIV弹窗
        var modal = document.getElementById('myModal');

        // 获取图片插入到弹窗 - 使用 "alt" 属性作为文本部分的内容
        var img = document.getElementById('myImg');
        var modalImg = document.getElementById("img01"); //获取弹出图片元素
        var captionText = document.getElementById("caption"); //获得文本描述
        img.onclick = function openImage() { //注册原图片点击事件
            modal.style.display = "block"; //此元素将显示为块级元素，此元素前后会带有换行符。
            modalImg.src = this.src; //将原图片URL赋给弹出图片元素
            captionText.innerHTML = this.alt; //赋值文本内容给弹出框文本
        }

        // 获取 <span> 元素，样式设置为关闭按钮
        var span = document.getElementsByClassName("close")[0];

        // 当点击 (x), 关闭弹窗
        span.onclick = function () {
            modal.style.display = "none"; //将模态框属性设置为不可见
        }
    }
