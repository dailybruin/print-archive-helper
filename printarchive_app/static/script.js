var g = $("#pdf-frame")
//
//.find("a:first").click();
g.on('load', function() {
  var loaded_btn = $("#pdf-frame").contents().find(".BRicon.zoom_in")
  console.log(loaded_btn)
});
