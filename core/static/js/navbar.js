
/* Listener para mover o seletor para a página ativa
 * toda vez que a página mudar */
window.addEventListener('DOMContentLoaded', (event) => {
    // Registra o nome da página atual
    const currentPage = window.location.pathname.split('/').pop();
    // Seleciona todos os links da navbar
    const links = document.querySelectorAll('.nav-links a');

    // Verifica qual dos links está ativo
    links.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage) {
            // Adiciona a classe 'active' ao link atual
            link.classList.add('active');
        }
    });
    
    // Seleciona o seletor
    const selector = document.querySelector('.nav-parent .selector');
    // Recupera a posição do seletor da página anterior
    const previousPos = localStorage.getItem('previousPos') || '0px';


    //Mudança para escolher a partir do título da página
    // Define a posição do seletor com base na página ativa
    switch(document.title) {
        
        case 'Sabidinhos - Home':
            selector.animate([
                { left: `${previousPos}` },
                { left: '40px' }
            ], { duration: 200 });

            selector.style.left = '40px';
            break;

        case 'Sabidinhos - Videos':
            selector.animate([
                { left: `${previousPos}` },
                { left: '120px' }
            ], { duration: 200 });

            selector.style.left = '120px';
            break;

        case 'Sabidinhos - Fórum':
            selector.animate([
                { left: `${previousPos}` },
                { left: '205px' }
            ], { duration: 200 });

            selector.style.left = '205px';
            break;

        case 'Sabidinhos - Pais e Professores':
            selector.animate([
                { left: `${previousPos}` },
                { left: '310px' }
            ], { duration: 200 });

            selector.style.left = '310px';
            break;

        default:
            selector.style.left = '40px';
            //selector.style.display = 'block';
            break;
    }

    /* Salva a posição do seletor no cache para ser
     * recuperada na página seguinte */
    localStorage.setItem('previousPos', selector.style.left);

    console.log("Active page: " + currentPage);
});
