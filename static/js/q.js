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