function set(totalBirres){
    totalBirres = {
  aInternal: 10,
  aListener: function(val) {},
  set a(val) {
    this.aInternal = val;
    this.aListener(val);
  },
  get a() {
    return this.aInternal;
  },
  registerListener: function(listener) {
    this.aListener = listener;

  }
}
document.getElementById("totalBirres").innerHTML = "hi there fuck you";
totalBirres.registerListener(function(val) {
  document.getElementById("totalBirres").innerHTML = totalBirres;
});

}

function test(){
  document.getElementById("totalBirres").innerHTML="Hi there"
}