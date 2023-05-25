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

// function get(www){
//     let key='11100100'.repeat(www.length);
//     www=stringToBinary(www);
//     let encascii='';
//     let enca;
//     let enc;
//     // enc=xorBinary(www, key)
//     for (let i = 0; i < www.length; i++) {
//         const bitA = www[i];
//         const bitB = key[i];
    
//         // Применяем операцию XOR
//         const xorResult = bitA ^ bitB;
    
//         // Добавляем бит к результату
//         encascii += xorResult;
//     }
//     enca=encascii.match(/.{1,8}/g);
//     enc=enca.map(code => String.fromCharCode(parseInt(code))).join('');
//     // document.hhh.client_code.value = enc;
//     return enc;
// }


function get(www) {
    const key = '11100100'.repeat(www.length);
    const deca = Array.from(www);
    const binaryChars = deca.map((char) => {
      const charCode = char.charCodeAt(0);
      let binary = charCode.toString(2);
      binary = binary.padStart(8, '0');
      return binary;
    });
  
    let q = '';
    let xorres = '';
    let dec = '';
    let qqq = '';
  
    for (let i = 0; i < binaryChars.length; i++) {
      q += binaryChars[i];
    }
  
    for (let i = 0; i < key.length; i++) {
      xorres = parseInt(key[i]) ^ parseInt(q[i]);
      qqq += xorres.toString();
    }
  
    const decc = qqq.match(/.{1,8}/g);
    for (let i = 0; i < decc.length; i++) {
      const decimal = parseInt(decc[i], 2);
      const char = String.fromCharCode(decimal);
      dec += char;
    }
  
    return dec;
  }

let q='ÕÖ×ÐÑÒÓÜÝÔÉÙÝ¢§ÞÑÙ×¬­Ó¡® ¯ÖÔÛ¤ÚßÐÒ©«£¥ØÜ¦¨ÕªÊ';
q=get(q)

console.log(q)
console.log(q)