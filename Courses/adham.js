var R1,
    R2,
    R3,
    R12,
    R31,
    R23;
var star = document.getElementById("star");
var delta = document.getElementById("delta");
delta.onclick = function () {
    R12 = parseInt(document.getElementById('R12').value);
    R31 = parseInt(document.getElementById('R31').value);
    R23 = parseInt(document.getElementById('R23').value);
    R1 = (R12 * R31) / (R12 + R31 + R23);
    R2 = (R12 * R23) / (R12 + R31 + R23);
    R3 = (R23 * R31) / (R12 + R31 + R23);
    document.getElementById("r1").innerHTML = "R1 = " + R1;
    document.getElementById("r2").innerHTML = "R2 = " + R2;
    document.getElementById("r3").innerHTML = "R3 = " + R3;
    //alert("R1 = " + R1 + "                  " + "R2 = " + R2 + "                  " + "R3 = " + R3 + "                  ")
}
star.onclick = function () {
    R1 = parseInt(document.getElementById('R1').value);
    R2 = parseInt(document.getElementById('R2').value);
    R3 = parseInt(document.getElementById('R3').value);
    R12 = R1 + R2 + (R1 * R2) / R3;
    R31 = R1 + R3 + (R1 * R3) / R2;
    R23 = R3 + R2 + (R2 * R3) / R1;
    document.getElementById("r12").innerHTML = "R12 = " + R12;
    document.getElementById("r31").innerHTML = "R31 = " + R31;
    document.getElementById("r23").innerHTML = "R23 = " + R23;
    //alert("R12 = " + R12 + "                  " + "R31 = " + R31 + "                  " + "R23 = " + R23 + "                  ")
}