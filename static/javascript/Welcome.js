var images = ["battlefieldv.jpg", "Fallout.jpg", "StarCraft II.jpg"];
    $(function () {
        var i = 0;
        $(".image_changer").css("background-image", "url(images/" + images[i] + ")");
        setInterval(function () {
            i++;
            if (i == images.length) {
                i = 0;
            }
            $(".image_changer").fadeOut("slow", function () {
                $(this).css("background-image", "url(images/" + images[i] + ")");
                $(this).fadeIn("slow");
            });
        }, 5000);
    });
