
function filter(video,canvas) {
    this.video=video;
    this.canvas=canvas;
    this.canvas.width=this.video.clientWidth;
    this.canvas.height=this.video.clientHeight-50;

    this.buffer_canvas= document.createElement("canvas");
    this.buffer_canvas.width=this.video.clientWidth;
    this.buffer_canvas.height=this.video.clientHeight-50;
    this.buffer_view=this.buffer_canvas.getContext("2d");
    this.filttered_view=canvas.getContext("2d");
    var self=this;
    this.addEventListener( "resize", function (e) {
      self.canvas.width = this.video.videoWidth;
      self.canvas.height = this.video.videoHeight;
    }, false );

     this.render = function () {
       if(!this.video.paused&&!this.video.ended){
         //var i=window.setInterval(function() {ctx.drawImage(v,0,0,270,135)},20);
         this.frame_filter();
       }
     }
     this.frame_filter = function () {
       this.buffer_view.drawImage(this.video,0,0,this.canvas.width,this.canvas.height);
       var data= this.buffer_view.getImageData(0,0,this.canvas.width,this.canvas.height);
       this.filttered_view.putImageData(data,0,0);
       StackBlur.canvasRGBA(this.canvas,0,8,this.canvas.width,23,15);
       // this.filttered_view.rect(0,8,this.canvas.width,23)
       StackBlur.canvasRGBA(this.canvas,this.canvas.width-170,this.canvas.height-60,130,60,15);
       //this.filttered_view.rect(this.canvas.width-165,this.canvas.height-60,130,60);
       this.filttered_view.stroke();
       return;
     }
  // self.render();
  this.video.addEventListener("play",function (){
      var i=window.setInterval(function() {self.render();},20);
    },false);

}