const rgbToHex = (r, g, b) => "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);

$("button.btn").on(
    "click", function() {
        const int = parseInt;

        var $temp = $("<input>");
        $("body").append($temp);

        var rgb = $(this).css("background-color").replace(")", "").replace("rgb(", "").split(", ")

        $temp.val(rgbToHex(int(rgb[0]), int(rgb[1]), int(rgb[2]))).select();
        document.execCommand("copy");
        $temp.remove();

        alert("Color Copied To Clipboard");
    }
);