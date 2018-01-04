function star()
{
    bigger();
}
function bigger()
{
    var ooo =document.getElementsByName("hoge001");
    var foo ="<center><hr><h3><font color=blue>日記帳</font></h3><h4>現在時刻 : ～～</h4><hr></center>";
    var bar ='<div class=Diary name="Diary"></div>';
    foo = foo.concat(bar);
    ooo[0].innerHTML = foo;
    
    var art = "";
    var art01 ='<form class =Article name="TodaysEvents">TodaysEvents</form>'
    var art02 ='<form class =Article name="TodaysNews">TodaysNews</form>'
    var art03 ='<div class =Article name="TodaysSchedule">TodaysSchedule</div>'
    var art04 ='<div class =Article name="ExperienceAndFeel">ExperienceAndFeel</div>'
    art = art.concat(art01);
    art = art.concat(art02);
    art = art.concat(art03);
    art = art.concat(art04);
    
    var KKK =document.getElementsByName("Diary");
    KKK[0].innerHTML = art;
}
window.onload = star;
