let counter = 1

const buttons = [
 {
   name: "Animatsioon",
 },
 {
   name: "Helindamine",
 },
 {
   name: "Graafika",
 },
 {
   name: "3D Graafika",
 },
 {
   name: "Video",
 },
 {
   name: "Veebiarendus",
 },
 {
   name: "Foto tööde",
 },
]

buttons.forEach(element=>{
  let button=document.createElement("button")
  button.classList = `btn-index-type btn${counter}-index`
  button.type = "button"
  button.textContent=element.name
  button.onclick = function(){alert(element.name)}
  document.querySelector(".form-btn-type").appendChild(button);
  counter++ 
})

