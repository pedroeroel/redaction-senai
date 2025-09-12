const argumentData = {
    educacao: [
        {
            title: "Desigualdade de acesso à educação de qualidade",
            content: "Muitos estudantes, especialmente de regiões periféricas e áreas rurais, não têm acesso a escolas com estrutura adequada, bons materiais didáticos e professores qualificados. Isso amplia a desigualdade social e limita as chances de ascensão, perpetuando um ciclo vicioso.",
            repertory: "Conceito de 'apartheid social' de Milton Santos, que aborda a segregação socioespacial e a exclusão de grupos da cidadania plena. Constituição Federal de 1988 (Art. 205): 'A educação, direito de todos e dever do Estado e da família, será promovida e incentivada com a colaboração da sociedade, visando ao pleno desenvolvimento da pessoa, seu preparo para o exercício da cidadania e sua qualificação para o trabalho.'",
            keywords: "desigualdade educacional, acesso, infraestrutura, qualidade de ensino, periferia, rural, exclusão social, Constituição"
        },
        {
            title: "Falta de investimento e gestão pública eficiente",
            content: "A má distribuição de recursos e a corrupção em alguns setores da administração pública afetam diretamente a qualidade da educação, principalmente na rede pública, que depende desses investimentos para melhorar sua estrutura e rendimento. Sem priorização, os desafios persistem.",
            repertory: "Dados do OCDE (Organização para a Cooperação e Desenvolvimento Econômico) que mostram o baixo investimento do Brasil em educação comparado a países desenvolvidos. Princípios da Administração Pública (legalidade, impessoalidade, moralidade, publicidade e eficiência) - Art. 37 da Constituição Federal.",
            keywords: "investimento público, corrupção, gestão, qualidade, rede pública, ineficiência"
        },
        {
            title: "Evasão escolar e o impacto na formação profissional",
            content: "A alta taxa de abandono escolar, principalmente no ensino médio, está ligada a fatores socioeconômicos (necessidade de trabalhar), falta de atratividade do modelo de ensino e violência. Isso resulta em menor qualificação, dificuldade de inserção no mercado de trabalho e precarização da mão de obra.",
            repertory: "Dados do Pnad Contínua (IBGE) sobre o abandono escolar. Teoria do Capital Humano, que ressalta a importância da educação para a produtividade e o desenvolvimento econômico de um país. Filósofo Paulo Freire e a 'pedagogia do oprimido', que defende a educação como ferramenta de libertação e transformação social.",
            keywords: "evasão escolar, abandono, ensino médio, mercado de trabalho, qualificação, socioeconômico"
        },
        {
            title: "Qualidade do ensino público X privado e o reflexo no ENEM",
            content: "A diferença de desempenho entre escolas públicas e privadas no ENEM e em outras avaliações demonstra a disparidade na qualidade da educação oferecida, impactando diretamente o acesso ao ensino superior e as oportunidades futuras. Essa dicotomia acentua a estratificação social.",
            repertory: "Resultados do ENEM e SAEB, comparando o desempenho de estudantes de redes pública e privada. Ideia de Pierre Bourdieu sobre 'capital cultural', onde a escola reproduz desigualdades sociais ao valorizar saberes da elite.",
            keywords: "ENEM, ensino público, ensino privado, desempenho, acesso superior, desigualdade"
        },
        {
            title: "Desvalorização do professor e a precarização da carreira docente",
            content: "Salários baixos, falta de planos de carreira, condições de trabalho inadequadas e violência nas escolas levam à desmotivação e à escassez de profissionais qualificados. Essa precarização compromete a base do ensino no país, impactando diretamente a qualidade do aprendizado.",
            repertory: "LDB (Lei de Diretrizes e Bases da Educação Nacional) que prevê a valorização dos profissionais da educação. Relatórios da UNESCO sobre a importância da valorização docente para sistemas educacionais de sucesso.",
            keywords: "professor, valorização docente, carreira, salário, condições de trabalho, precarização, qualidade do ensino"
        }
    ],
    meio: [
        {
            title: "Desmatamento e perda da biodiversidade",
            content: "A destruição de florestas, como a Amazônia, o Cerrado e a Mata Atlântica, compromete o equilíbrio ecológico, causa a extinção de espécies e afeta os ciclos da água e do clima. O desmatamento também favorece o aumento de queimadas e libera grandes quantidades de carbono na atmosfera, intensificando o efeito estufa.",
            repertory: "Conceito de 'Crise Ambiental' de Edgar Morin. 'A Primavera Silenciosa' de Rachel Carson, obra que alertou sobre os impactos dos pesticidas na natureza. Art. 225 da Constituição Federal: 'Todos têm direito ao meio ambiente ecologicamente equilibrado, bem de uso comum do povo e essencial à sadia qualidade de vida...'",
            keywords: "desmatamento, biodiversidade, Amazônia, ecossistema, queimadas, efeito estufa, sustentabilidade"
        },
        {
            title: "Poluição e seus impactos na saúde e na natureza",
            content: "A poluição do ar (indústria, veículos), da água (esgoto, agrotóxicos) e do solo (descarte inadequado de resíduos) afeta a saúde humana (doenças respiratórias, contaminação), prejudica os ecossistemas aquáticos e terrestres e contamina os recursos naturais essenciais à vida.",
            repertory: "Conferência de Estocolmo (1972) e Rio-92 (1992), marcos na discussão ambiental global. Relatórios da OMS (Organização Mundial da Saúde) sobre o impacto da poluição do ar na mortalidade. Conceito de 'Antropoceno', era geológica marcada pela ação humana.",
            keywords: "poluição, ar, água, solo, saúde, ecossistemas, resíduos, sustentabilidade"
        },
        {
            title: "Crise hídrica e a gestão da água no Brasil",
            content: "A escassez de água em diversas regiões do país, agravada pelo desperdício (uso doméstico e industrial), poluição dos rios e má gestão dos recursos hídricos, ameaça o abastecimento, a agricultura e a segurança alimentar da população. A falta de chuvas e o aumento do consumo intensificam o problema.",
            repertory: "Dados da ANA (Agência Nacional de Águas) e IBGE sobre disponibilidade hídrica e consumo. A Crise da Água em São Paulo (2014-2015) como estudo de caso. Conceito de 'pegada hídrica'.",
            keywords: "crise hídrica, escassez de água, gestão hídrica, desperdício, poluição, segurança alimentar"
        },
        {
            title: "Aumento de eventos climáticos extremos e suas consequências",
            content: "Secas prolongadas, inundações, ondas de calor recordes e tempestades severas são cada vez mais frequentes, causando desabrigados, perdas econômicas (agricultura, infraestrutura) e impactos severos na saúde pública. O Brasil tem sido palco de diversos desses eventos nos últimos anos.",
            repertory: "Relatórios do IPCC (Painel Intergovernamental sobre Mudanças Climáticas). Acordo de Paris sobre o Clima. A Teoria de James Lovelock sobre Gaia (o planeta como um superorganismo autorregulador, que reage às perturbações).",
            keywords: "eventos climáticos, mudanças climáticas, desastres naturais, aquecimento global, sustentabilidade, impactos"
        },
        {
            title: "Descarte inadequado de lixo e a contaminação do solo e da água",
            content: "A falta de saneamento básico adequado e de políticas eficazes de reciclagem e compostagem no Brasil leva ao acúmulo de lixo em lixões a céu aberto e aterros irregulares, contaminando o solo, a água subterrânea e causando problemas de saúde pública, além de poluir visualmente as cidades.",
            repertory: "PNRS (Política Nacional de Resíduos Sólidos). Conceito de 'logística reversa'. Dados do SNIS (Sistema Nacional de Informações sobre Saneamento) sobre a cobertura de coleta e tratamento de lixo no Brasil.",
            keywords: "lixo, descarte, saneamento básico, reciclagem, contaminação, saúde pública, resíduos sólidos"
        }
    ],
    saude: [
        {
            title: "Desigualdade no acesso aos serviços de saúde",
            content: "No Brasil, o acesso à saúde de qualidade ainda é desigual. Enquanto grandes centros urbanos contam com mais hospitais e profissionais especializados, regiões rurais e periféricas sofrem com a falta de infraestrutura, leitos, equipamentos e médicos, o que compromete o atendimento e o bem-estar da população.",
            repertory: "Art. 196 da Constituição Federal: 'A saúde é direito de todos e dever do Estado, garantido mediante políticas sociais e econômicas que visem à redução do risco de doença e de outros agravos e ao acesso universal e igualitário às ações e serviços para sua promoção, proteção e recuperação.' Conceito de 'saúde como direito universal'.",
            keywords: "desigualdade, acesso à saúde, SUS, infraestrutura, periferia, rural, direito à saúde"
        },
        {
            title: "Superlotação e falta de recursos no sistema público (SUS)",
            content: "O Sistema Único de Saúde (SUS), apesar de sua importância e abrangência, enfrenta problemas crônicos como a superlotação de hospitais, longas filas de espera, falta de médicos especialistas, equipamentos defasados e escassez de medicamentos. Isso prejudica diagnósticos precoces e tratamentos eficazes.",
            repertory: "Princípios do SUS (universalidade, integralidade, equidade). Relatórios do Conselho Nacional de Saúde e Ministério da Saúde sobre o subfinanciamento do SUS. O médico sanitarista Sergio Arouca e sua defesa da saúde pública universal.",
            keywords: "SUS, superlotação, recursos, saúde pública, financiamento, fila de espera"
        },
        {
            title: "Prevenção e combate a doenças endêmicas (ex: dengue)",
            content: "A falta de saneamento básico, o acúmulo de lixo, a urbanização desordenada e a deficiência em campanhas de conscientização contribuem para a proliferação de doenças como a dengue, zika, chikungunya e febre amarela. Essas epidemias sobrecarregam o sistema de saúde e causam grandes impactos sociais e econômicos.",
            repertory: "Dados do Ministério da Saúde sobre incidência de doenças endêmicas. Conceito de 'determinantes sociais da saúde'. A figura de Oswaldo Cruz e suas campanhas sanitárias no início do século XX.",
            keywords: "doenças endêmicas, dengue, zika, chikungunya, saneamento básico, prevenção, saúde pública"
        },
        {
            title: "Saúde mental e o aumento de transtornos psicológicos",
            content: "O estigma em relação às doenças mentais, a falta de acesso a tratamento psicológico e psiquiátrico (especialmente na rede pública), as pressões sociais e o ritmo de vida moderno contribuem para o aumento alarmante de casos de depressão, ansiedade, burnout e outros transtornos, especialmente entre jovens e trabalhadores.",
            repertory: "Dados da OMS (Organização Mundial da Saúde) que indicam o Brasil como um dos países com maior prevalência de ansiedade e depressão. Luta Antimanicomial no Brasil. O impacto da pandemia de COVID-19 na saúde mental.",
            keywords: "saúde mental, transtornos psicológicos, depressão, ansiedade, estigma, acesso a tratamento"
        },
        {
            title: "Acesso a medicamentos e tratamentos de alto custo",
            content: "Pacientes com doenças crônicas ou raras enfrentam enormes dificuldades para obter medicamentos e tratamentos de alto custo, seja pela burocracia do SUS, pela falta de disponibilidade de terapias inovadoras ou pelo preço proibitivo na rede privada. Isso gera judicialização da saúde e desespero para muitas famílias.",
            repertory: "Decisões do STF (Supremo Tribunal Federal) sobre o direito à saúde e fornecimento de medicamentos. O caso de doenças raras e os desafios de pesquisa e produção de terapias. O princípio da 'dignidade da pessoa humana'.",
            keywords: "medicamentos de alto custo, tratamento, doenças raras, judicialização, SUS, acesso"
        }
    ],
    tecnologia: [
        {
            title: "Tecnologia como ferramenta de progresso social",
            content: "A tecnologia tem revolucionado áreas essenciais como saúde, educação, transporte e comunicação. Inovações como a telemedicina, plataformas de ensino a distância, internet 5G e inteligência artificial (IA) otimizam serviços, aumentam o acesso da população a direitos básicos e impulsionam o desenvolvimento econômico e social.",
            repertory: "Conceito de 'sociedade da informação' e 'revolução tecnológica'. A Indústria 4.0. Exemplos como o aplicativo SUS Conectado ou plataformas de e-learning que democratizam o conhecimento.",
            keywords: "tecnologia, progresso social, inovação, telemedicina, EAD, inteligência artificial, desenvolvimento"
        },
        {
            title: "Exclusão digital e aprofundamento das desigualdades sociais",
            content: "Apesar do avanço tecnológico, milhões de brasileiros ainda vivem sem acesso à internet de qualidade ou a dispositivos digitais. Essa exclusão limita o acesso à informação, à educação online, a serviços públicos digitalizados e a oportunidades no mercado de trabalho, aprofundando as desigualdades já existentes.",
            repertory: "Dados do Cetic.br (Centro Regional de Estudos para o Desenvolvimento da Sociedade da Informação) sobre o acesso à internet no Brasil, evidenciando as disparidades regionais e socioeconômicas. Conceito de 'cidadania digital'.",
            keywords: "exclusão digital, desigualdade social, acesso à internet, inclusão digital, mercado de trabalho"
        },
        {
            title: "Cibersegurança e os desafios de proteção de dados",
            content: "Com o aumento exponencial do uso da internet e da digitalização de serviços, crescem também os riscos de ataques cibernéticos, vazamento de dados pessoais e fraudes online. A falta de segurança digital pode comprometer a privacidade dos usuários, a segurança de instituições e a estabilidade de sistemas essenciais, exigindo legislação e educação robustas.",
            repertory: "LGPD (Lei Geral de Proteção de Dados Pessoais). Casos recentes de vazamento de dados no Brasil e no mundo. O debate sobre 'direito ao esquecimento' e privacidade na era digital.",
            keywords: "cibersegurança, proteção de dados, LGPD, privacidade, vazamento de dados, crimes cibernéticos"
        },
        {
            title: "O impacto das redes sociais na saúde mental e na sociedade",
            content: "Embora conectem pessoas, as redes sociais podem contribuir para problemas de saúde mental, como ansiedade, depressão e distúrbios de imagem, devido à comparação social constante, ao cyberbullying e à disseminação de notícias falsas. Isso afeta a coesão social e a percepção da realidade, exigindo letramento digital e moderação.",
            repertory: "Documentário 'O Dilema das Redes'. Conceito de 'infodemia'. Estudos da Sociedade Brasileira de Pediatria sobre o impacto do uso excessivo de telas em crianças e adolescentes. A 'Bolha Social' ou 'Câmara de Eco'.",
            keywords: "redes sociais, saúde mental, cyberbullying, fake news, coesão social, letramento digital"
        },
        {
            title: "Inteligência Artificial (IA) e o futuro do trabalho",
            content: "A ascensão da IA e da automação traz debates importantes sobre a substituição de empregos, a necessidade de requalificação profissional e a criação de novas funções. A IA tem o potencial de otimizar processos, mas também exige uma adaptação da força de trabalho e políticas públicas para mitigar impactos sociais e econômicos negativos.",
            repertory: "Asimov e suas 'Três Leis da Robótica'. Livro 'Sapiens: Uma Breve História da Humanidade' de Yuval Noah Harari, que discute o futuro do trabalho. O debate sobre 'renda básica universal' em cenários de alta automação.",
            keywords: "Inteligência Artificial, IA, automação, mercado de trabalho, requalificação, futuro do trabalho"
        }
    ],
    desigualdade: [
        {
            title: "Desigualdade social e concentração de renda",
            content: "No Brasil, uma pequena parcela da população detém a maior parte da riqueza, enquanto milhões vivem em situação de pobreza ou extrema pobreza. Essa concentração de renda gera exclusão social, dificulta o acesso a direitos básicos (saúde, moradia, educação) e acentua a marginalização de grupos vulneráveis.",
            repertory: "Dados do IBGE e do relatório da Oxfam Brasil sobre a concentração de renda no país. Conceito de 'luta de classes' de Karl Marx. A Teoria da Equidade de John Rawls.",
            keywords: "desigualdade social, concentração de renda, pobreza, exclusão social, privilégio, vulnerabilidade"
        },
        {
            title: "Desigualdade educacional como reflexo da desigualdade social",
            content: "Estudantes de escolas públicas, especialmente nas periferias e zonas rurais, enfrentam infraestrutura precária, falta de recursos e baixa qualidade de ensino, em contraste com a realidade do ensino privado. Isso limita suas chances no mercado de trabalho, no acesso à universidade e perpetua o ciclo da pobreza e da desigualdade.",
            repertory: "Resultados de avaliações como o PISA (Programa Internacional de Avaliação de Estudantes) que mostram a disparidade no desempenho entre estudantes de diferentes realidades socioeconômicas no Brasil. A teoria do 'habitus' de Pierre Bourdieu, que explica como as experiências sociais moldam indivíduos e reforçam desigualdades.",
            keywords: "desigualdade educacional, acesso, infraestrutura, qualidade de ensino, meritocracia, ciclo da pobreza"
        },
        {
            title: "Desigualdade de gênero e a violência contra a mulher",
            content: "A persistência da violência doméstica, feminicídio, assédio sexual e a diferença salarial entre homens e mulheres mostram que a desigualdade de gênero ainda é um problema grave no Brasil, com raízes históricas e culturais profundas. O machismo estrutural impacta diretamente a autonomia e segurança feminina.",
            repertory: "Lei Maria da Penha. Dados do Fórum Brasileiro de Segurança Pública sobre feminicídio. O movimento feminista e a luta por equidade. Simone de Beauvoir e a obra 'O Segundo Sexo', que discute a construção social do feminino.",
            keywords: "desigualdade de gênero, violência contra a mulher, feminicídio, machismo, equidade, direitos das mulheres"
        },
        {
            title: "Racismo estrutural e a desigualdade racial",
            content: "O racismo no Brasil se manifesta na dificuldade de acesso a empregos de qualidade (especialmente para cargos de liderança), na violência policial seletiva e na sub-representação da população negra em espaços de poder e no ensino superior. Isso evidencia uma estrutura social que perpetua a discriminação e a marginalização, apesar da miscigenação.",
            repertory: "Conceito de 'Racismo Estrutural' de Silvio Almeida. Lei Áurea e suas consequências sociais. Dados do IBGE sobre renda e escolaridade por raça. O movimento negro e a luta por direitos e reconhecimento. Gilberto Freyre e o mito da 'democracia racial' no Brasil.",
            keywords: "racismo estrutural, desigualdade racial, população negra, discriminação, acesso a direitos, miscigenação"
        },
        {
            title: "Acesso desigual à justiça e à segurança pública",
            content: "Pessoas de baixa renda, moradores de áreas periféricas e minorias frequentemente têm menos acesso a serviços jurídicos de qualidade e são mais vulneráveis à violência e à falta de segurança pública, seja pela ineficiência do Estado ou pela seletividade do sistema penal. Isso revela uma falha em garantir direitos básicos e a proteção igualitária a todos os cidadãos.",
            repertory: "A obra 'Vigiar e Punir' de Michel Foucault, que analisa as relações de poder e o sistema prisional. Dados sobre a população carcerária brasileira (majoritariamente negra e de baixa escolaridade). O conceito de 'estado de exceção' em comunidades pobres.",
            keywords: "acesso à justiça, segurança pública, desigualdade, sistema penal, direitos humanos, vulnerabilidade"
        }
    ]
};

// Ícones SVG para os botões de tema (ajustei alguns para serem mais genéricos/simbólicos)
const themeIcons = {
    educacao: `
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 0 0-.491 6.347m6.579-4.593A28.318 28.318 0 0 1 15 11.25c2.31 0 4.514.06 6.74.179m-9.778 8.645-4.782-1.837M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm6.36-2.904c-3.517-.4-7.016-.8-10.513-1.2l-2.244-.224m4.242 1.224L10.5 18.75 8.25 21.75m4.997-15.01a6.002 6.002 0 0 0-4.78 2.36M14.25 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
        </svg>
    `, // Educação - Círculo com símbolos de aprendizado
    meio: `
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 7.5l-9-5.25L3 7.5m18 0l-9 5.25m9-5.25v9l-9 5.25M3 7.5l9 5.25M3 7.5v9l9 5.25m0-9v9" />
        </svg>
    `, // Meio ambiente - Árvore ou folha
    saude: `
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
        </svg>
    `, // Saúde - Coração ou Cruz
    tecnologia: `
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 0 0 6 3.75v16.5a2.25 2.25 0 0 0 2.25 2.25h7.5A2.25 2.25 0 0 0 18 20.25V3.75A2.25 2.25 0 0 0 15.75 1.5H13.5m-3 0V3h3V1.5m-3 0h3l-3 0ZM9 18h6" />
        </svg>
    `, // Tecnologia - Chip ou Celular
    desigualdade: `
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12M12 6a6 6 0 0 0-6 6v6m6-12a6 6 0 0 1 6 6v6m-6-12V5.25M12 18V18.75" />
        </svg>
    ` // Desigualdade - Balança ou Pessoas em desnível
};

// JavaScript para Parallax e Animações no Scroll
const parallaxBg = document.getElementById('parallax-bg');
if (parallaxBg) {
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        parallaxBg.style.setProperty('--translate-y', `${scrollY * 0.15}px`);
    });
}
    
// Funções para a interação da página, como renderizar botões e o modal
const themeButtonsContainer = document.getElementById('themeButtonsContainer');
const argumentsDisplayArea = document.getElementById('argumentsDisplayArea');
const selectThemePrompt = document.getElementById('selectThemePrompt');

function renderThemeButtons() {
    for (const themeKey in argumentData) {
        const button = document.createElement('button');
        button.setAttribute('role', 'tab');
        button.setAttribute('aria-controls', `${themeKey}-arguments`);
        button.id = `tab-${themeKey}`;
        button.className = "flex items-center justify-center space-x-2 px-6 py-3 rounded-full text-lg font-semibold bg-[#2A0F5E] text-[#E8E1CF] shadow-lg hover:bg-[#5A3E9D] hover:scale-105 transition-all duration-300 ease-in-out cursor-pointer whitespace-nowrap border-2 border-transparent min-w-[160px]";
        button.innerHTML = `${themeIcons[themeKey]} <span>${themeKey.charAt(0).toUpperCase() + themeKey.slice(1).replace('-', ' ')}</span>`;
        button.onclick = () => mostrarArgumentos(themeKey, button);
        themeButtonsContainer.appendChild(button);
    }
}

function mostrarArgumentos(tema, clickedButton) {
    selectThemePrompt.style.display = 'none';

    const buttons = document.querySelectorAll('.temas button');
    buttons.forEach(button => {
        button.classList.remove('active', 'bg-[#FCA311]', 'text-[#1A0B3D]', 'border-[#FCA311]', 'shadow-2xl', 'scale-105');
        button.setAttribute('aria-selected', 'false');
        button.classList.add('bg-[#2A0F5E]', 'text-[#E8E1CF]', 'border-transparent', 'shadow-lg');
    });

    if (clickedButton) {
        clickedButton.classList.add('active', 'bg-[#FCA311]', 'text-[#1A0B3D]', 'border-[#FCA311]', 'shadow-2xl', 'scale-105');
        clickedButton.classList.remove('bg-[#2A0F5E]', 'text-[#E8E1CF]');
        clickedButton.setAttribute('aria-selected', 'true');
    }

    argumentsDisplayArea.innerHTML = '';

    const args = argumentData[tema];
    if (args) {
        args.forEach((arg, index) => {
            const card = document.createElement('button');
            card.classList.add('argumento-card', 'bg-[#3D1E8D]', 'p-6', 'rounded-xl', 'shadow-lg', 'hover:brightness-110', 'active:brightness-90', 'transition-all', 'duration-200', 'ease-in-out', 'transform', 'hover:-translate-y-2', 'flex', 'flex-col', 'justify-between', 'text-center', 'cursor-pointer', 'relative', 'overflow-hidden');
            card.setAttribute('role', 'button');
            card.setAttribute('aria-label', `Ver detalhes do argumento ${arg.title}`);
            card.innerHTML = `
                <h2 class="text-lg sm:text-xl font-semibold text-[#E8E1CF] mb-2 leading-snug">${arg.title}</h2>
                <p class="type text-sm text-[#C4B5FD] opacity-80 mt-auto">${arg.type || 'Argumento Geral'}</p> `;
            card.onclick = () => openModal(arg);
            card.style.animationDelay = `${index * 0.1}s`;
            argumentsDisplayArea.appendChild(card);
        });
    }
}
    
const argumentoModalOverlay = document.getElementById('argumentoModalOverlay');
const modalArgumentoTitle = document.getElementById('modalArgumentoTitle');
const modalArgumentoContent = document.getElementById('modalArgumentoContent');
const modalRepertoryContent = document.getElementById('modalRepertoryContent');
const modalKeywordsContent = document.getElementById('modalKeywordsContent');
const modalCopyButton = document.getElementById('modalCopyButton');

function openModal(arg) {
    modalArgumentoTitle.innerText = arg.title;
    modalArgumentoContent.innerText = arg.content;
    modalRepertoryContent.innerText = arg.repertory || 'Nenhum repertório sugerido para este argumento.';
    modalKeywordsContent.innerText = arg.keywords || 'Nenhuma palavra-chave sugerida.';

    modalCopyButton.dataset.copyContent = `Título: ${arg.title}\n\nArgumento: ${arg.content}\n\nRepertório: ${arg.repertory || 'Nenhum'}\n\nPalavras-chave: ${arg.keywords || 'Nenhuma'}`;

    modalCopyButton.innerText = "Copiar Argumento";
    modalCopyButton.classList.remove('copied');

    argumentoModalOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    argumentoModalOverlay.classList.remove('open');
    document.body.style.overflow = 'auto';
}

async function copiarTexto(textToCopy, buttonElement) {
    try {
        await navigator.clipboard.writeText(textToCopy);
        if (buttonElement) {
            buttonElement.innerText = "Copiado!";
            buttonElement.classList.add('copied');
            setTimeout(() => {
                buttonElement.innerText = "Copiar Argumento";
                buttonElement.classList.remove('copied');
            }, 1500);
        }
    } catch (err) {
        console.error('Falha ao copiar: ', err);
        alert('Erro ao copiar o texto. Por favor, tente novamente.');
    }
}

function copiarArgumentoModal(buttonElement) {
    const contentToCopy = buttonElement.dataset.copyContent;
    copiarTexto(contentToCopy, buttonElement);
}

document.addEventListener('DOMContentLoaded', () => {
    renderThemeButtons();
});