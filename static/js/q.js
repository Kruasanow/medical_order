function xorBinary(a, b) {
    // Преобразуем двоичные числа в строки
    const binaryA = a.toString();
    const binaryB = b.toString();
  
    // Получаем максимальную длину двоичных чисел
    const maxLength = Math.max(binaryA.length, binaryB.length);
  
    // Дополняем двоичные числа нулями слева до максимальной длины
    const paddedA = binaryA.padStart(maxLength, '0');
    const paddedB = binaryB.padStart(maxLength, '0');
  
    let result = '';
  
    // Выполняем операцию XOR между каждой парой битов
    for (let i = 0; i < maxLength; i++) {
      const bitA = paddedA[i];
      const bitB = paddedB[i];
  
      // Применяем операцию XOR
      const xorResult = bitA ^ bitB;
  
      // Добавляем бит к результату
      result += xorResult;
    }
  
    return result;
  }

function stringToBinary(string) {
    let binary = "";
    for (let i = 0; i < string.length; i++) {
      // Получаем числовое представление символа
      const decimal = string.charCodeAt(i);
      // Преобразуем числовое представление в двоичное число
      const binaryChar = decimal.toString(2).padStart(8, "0");
      binary += binaryChar;
    }
    return binary;
  }

function get(www){
    let key='11100100'.repeat(www.length);
    www=stringToBinary(www);
    let encascii='';
    let enca;
    let enc;
    // enc=xorBinary(www, key)
    for (let i = 0; i < www.length; i++) {
        const bitA = www[i];
        const bitB = key[i];
    
        // Применяем операцию XOR
        const xorResult = bitA ^ bitB;
    
        // Добавляем бит к результату
        encascii += xorResult;
    }
    enca=encascii.match(/.{1,8}/g);
    enc=enca.map(code => String.fromCharCode(parseInt(code))).join('');
    // document.hhh.client_code.value = enc;
    return enc;
}

function DoSubmit(){
    let www=document.hhh.client_code.value;
    document.hhh.client_code.value=get(www);

    www=document.hhh.fio.value;
    document.hhh.fio.value=get(www);
    
    www=document.hhh.address.value;
    document.hhh.address.value=get(www);

    www=document.hhh.phone.value;
    document.hhh.phone.value=get(www);
    
    www=document.hhh.email.value;
    document.hhh.email.value=get(www);
    
    www=document.hhh.other_data.value;
    document.hhh.other_data.value=get(www);
    
    www=document.hhh.animal_code.value;
    document.hhh.animal_code.value=get(www);
    
    www=document.hhh.kind.value;
    document.hhh.kind.value=get(www);
    
    www=document.hhh.poroda.value;
    document.hhh.poroda.value=get(www);
    
    www=document.hhh.klichka.value;
    document.hhh.klichka.value=get(www);
    
    www=document.hhh.sex.value;
    document.hhh.sex.value=get(www);
    
    www=document.hhh.bday.value;
    document.hhh.bday.value=get(www);
    
    www=document.hhh.color.value;
    document.hhh.color.value=get(www);
    
    www=document.hhh.info.value;
    document.hhh.info.value=get(www);

    return true;
  }