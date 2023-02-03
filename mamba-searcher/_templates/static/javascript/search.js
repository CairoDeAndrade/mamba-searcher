  function selecionado(selectElement){
    let valor = selectElement.innerHTML
    let barra = document.getElementById('select_words')
    if (barra.value == ''){
      barra.value = valor
    }else{
      barra.value += ',' + valor
    }
  }