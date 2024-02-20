(()=> {

    const $doc = document;
    const $button = $doc.getElementById('js__button');
    const $result = $doc.getElementById('result');

    $button.addEventListener('click', ()=> {

        const $serchWord = $doc.getElementById('js__serch').value;
        
        (async() => {

            const res = await fetch('serch', {
                method: 'POST',
                headers: {
                    'Content-Type': 'text/plain'
                },
                body: $serchWord
            })

            const resTxt = await res.text()
            $result.innerText = resTxt;

        })()
        
    })


})()