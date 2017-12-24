function start()
{
    //テンプレート文字列をロード
    var path = window.external.ThrowTemplatePath();
    var flame =document.getElementsByName("Tamplate");
    flame[0].innerHTML = path;
    
    //保存先パス文字列をロード
    var foo = window.external.ThrowSavePath();
    var ooo =document.getElementsByName("PathOfSave");
    ooo[0].innerHTML = foo;
    
    //テンプレートをロード
    var info = window.external.Load(flame[0].innerHTML);
    var obj = JSON.parse(info);
    
    //g チャプターの中の種別選択
    var ChapterSelect = obj.Index.Contents.Chapter.sumTotal;
    for(var g=1;g<=ChapterSelect;g++){
        
        var ChapterName = obj.Index.Contents.Chapter["n"+String(g)]["name"];
        var ChapterSubject = obj.Index.Contents.Chapter["n"+String(g)]["Subject"];
        var ChapterSubstance = obj.Index.Contents.Chapter["n"+String(g)]["Substance"];
        var sbj = document.getElementsByName("Subject_"+ChapterName);
        var sbs = document.getElementsByName("Substance_"+ChapterName);
        sbj[0].innerHTML = ChapterSubject;
        sbs[0].innerHTML = ChapterSubstance;
        
        //i 初期項目数設定
        var initualTimes = obj.Index.Contents.Chapter["n"+String(g)]["initualTimes"];
        
        //j 項目の中のform数
        var sumTotal = obj.Index.Contents.Chapter["n"+String(g)]["item"]["Questions"]["sumTotal"];
        for(var i=1;i<=initualTimes;i++){
            for(var j=1;j<=sumTotal;j++){
                var ChapterNumber = document.getElementsByName(ChapterName+"_"+String(i)+"_num");
                ChapterNumber[0].innerHTML = String(i);
                var Qwrite = document.getElementsByName(ChapterName+"_"+String(i)+"_Question"+String(j));
                Qwrite[0].innerHTML = obj.Index.Contents.Chapter["n"+String(g)]
                        ["item"]["Questions"]["n"+String(j)]["article"];
            }
        }
    }
}
window.onload = start;
//----------------------------------------------------
function PathOfSave_Botton_Click()
{
    var loadPath = window.external.OpenDirDialog();
    alert(loadPath);
    var POS= document.getElementsByName("PathOfSave");
    POS[0].innerHTML  = loadPath;
}
function JsonSave(str)
{
    //テンプレートをロード
    var temp =document.getElementsByName("Tamplate");
    var info = window.external.Load(temp[0].innerHTML);
    var TemplateObject = JSON.parse(info);
    
    //ChapSumTotal チャプター数
    var ChapSumTotal = TemplateObject.Index.Contents.Chapter.sumTotal;
    
    //Chapters テンプレートのチャプター文字列、チャプター番号を格納
    var Chapters = new Array();
    for(var k=1;k<=ChapSumTotal;k++){
        Chapters[k]=TemplateObject.Index.Contents.Chapter["n"+String(k)]["name"];
    }
    
    //nameによってチャプターを選択する
    var chooseChap = 0;
    for(var g=1;g<=ChapSumTotal;g++){
        if(Chapters[g]==str){
            chooseChap=g;
        }
    }
    //----------------------------------------------------//
    //既存の今日のデータをロード
    var PoS =document.getElementsByName("PathOfSave");
    var LoadExistFile = window.external.Load(PoS[0].innerHTML);
    var JsonData = null;
    
    if(LoadExistFile!=""){
        //既存のデータが存在するとき
        JsonData = JSON.parse(LoadExistFile);
        alert(JSON.stringify(JsonData));
    }else{
        //既存のデータが存在しない時
        var JsonData = new Object();
        JsonData.QandA =new Object();
    }
    JsonData.QandA[str] =new Object();
    //----------------------------------------------------//
    
    //i 初期項目数設定
    var initualTimes = TemplateObject.Index.Contents.Chapter["n"+String(chooseChap)]["initualTimes"];
    
    //j 項目の中のform数
    var sumTotal = TemplateObject.Index.Contents.Chapter["n"+String(chooseChap)]
                   ["item"]["Questions"]["sumTotal"];
    
    for(var i=1;i<=initualTimes;i++){
        JsonData.QandA[str][str+"_"+String(i)] =new Object();
        for(var j=1;j<=sumTotal;j++){
            JsonData.QandA[str][str+"_"+String(i)][str+"_"+String(i)+"_"+String(j)] =new Object();
            var Q11=document.getElementsByName(str+"_"+String(i)+"_Question"+String(j));
            var A11=document.getElementsByName(str+"_"+String(i)+"_Answer"+String(j));
            JsonData.QandA[str][str+"_"+String(i)][str+"_"+String(i)+"_"+String(j)].Q =Q11[0].innerHTML;
            JsonData.QandA[str][str+"_"+String(i)][str+"_"+String(i)+"_"+String(j)].A =A11[0].value;
        }
    }
    
    var mani = JSON.stringify(JsonData);
    var TEJson = document.getElementsByName(str+"_JsonString");
    TEJson[0].innerHTML = mani;
    
    var path = document.getElementsByName("PathOfSave");
    alert(path[0].innerHTML);
    window.external.Save(path[0].innerHTML,mani);
}
