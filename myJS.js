$(function () {
    $("button").hover(
        function () {
            $(this).css("color", "#00f");
            $("p").hide();
        }
        ,
        function () {
            $(this).css("color", "#f00");
            $("p").show();
            $("p").css("color", "green");
        }
    );
});