function reverse () {{
    const value_selecteurA = document.getElementsByClassName('bsa')[0].value;
    const value_selecteurB = document.getElementsByClassName('bsb')[0].value;
    document.getElementsByClassName(value_selecteurB)[0].selected = true;
    document.getElementsByClassName(value_selecteurA)[1].selected = true;
}}