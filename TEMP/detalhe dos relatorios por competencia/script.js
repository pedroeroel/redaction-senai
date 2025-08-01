document.addEventListener('DOMContentLoaded', () => {
    const competenciaButtonsContainer = document.getElementById('competencia-buttons-container'); // Novo: Onde os botões serão inseridos
    let competenciaButtons; // Vai armazenar os botões depois de criados

    const personagemContainer = document.getElementById('personagem-container');
    const detalhesContainer = document.getElementById('competencia-detalhes-container');
    const btnFecharDetalhes = document.getElementById('btn-fechar-detalhes'); // Botão de fechar/voltar

    const tituloDetalhes = document.getElementById('competencia-titulo');
    const notaDetalhes = document.getElementById('competencia-nota');
    const comentariosDetalhesP = document.getElementById('competencia-comentarios').querySelector('p');
    const dicasDetalhesP = document.getElementById('competencia-dicas').querySelector('p');

    // Dados de exemplo para cada competência
    const dadosCompetencias = {
        1: {
            titulo: "Competência 1",
            nota: "200/200",
            comentarios: "Análise da Competência 1: Demonstrar domínio da modalidade escrita formal da língua portuguesa. Sua redação apresentou excelente coesão e coerência, com poucos ou nenhum desvio gramatical.",
            dicas: "Para manter o alto nível, revise sempre a concordância verbal e nominal, e o uso adequado da crase. Continue praticando a leitura para ampliar seu vocabulário."
        },
        2: {
            titulo: "Competência 2",
            nota: "180/200",
            comentarios: "Análise da Competência 2: Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais do texto dissertativo-argumentativo em prosa.",
            dicas: "Busque diversificar seus argumentos e repertório sociocultural. Cite filósofos, dados estatísticos ou fatos históricos relevantes para enriquecer sua argumentação."
        },
        3: {
            titulo: "Competência 3",
            nota: "160/200",
            comentarios: "Análise da Competência 3: Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista.",
            dicas: "Certifique-se de que seus parágrafos de desenvolvimento estão bem estruturados, com tópico frasal, desenvolvimento da ideia e conclusão. A ligação entre os argumentos deve ser clara."
        },
        4: {
            titulo: "Competência 4",
            nota: "200/200",
            comentarios: "Análise da Competência 4: Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação.",
            dicas: "Excelente uso de conectivos! Mantenha essa prática, variando os operadores argumentativos para evitar repetições e garantir a fluidez do texto."
        },
        5: {
            titulo: "Competência 5",
            nota: "190/200",
            comentarios: "Análise da Competência 5: Elaborar proposta de intervenção para o problema abordado, respeitando os direitos humanos.",
            dicas: "Sua proposta de intervenção foi boa, mas poderia ser mais detalhada. Lembre-se de apresentar o agente, a ação, o meio/modo, a finalidade e um detalhamento da proposta."
        }
    };

    // Função para criar os botões de competência dinamicamente
    function criarBotoesCompetencia() {
        // Percorre as chaves do objeto dadosCompetencias
        for (const id in dadosCompetencias) {
            // Cria um novo elemento de botão
            const button = document.createElement('button');
            // Adiciona as classes Tailwind CSS e a classe 'competencia-btn'
            button.className = "competencia-btn w-full text-[#E8E1CF] border-2 border-[#E8E1CF] rounded-full py-3 px-6 text-sm sm:text-base font-medium hover:bg-[#E8E1CF] hover:text-[#3D1E8D] transition-colors duration-200";
            // Adiciona o atributo data-competencia com o ID da competência
            button.dataset.competencia = id;
            // Define o texto do botão
            button.textContent = `competência ${id}`;
            // Adiciona o botão ao container no HTML
            competenciaButtonsContainer.appendChild(button);
        }
        // Atualiza a NodeList de botões após a criação dinâmica
        competenciaButtons = document.querySelectorAll('.competencia-btn');
        // Adiciona os event listeners após a criação dos botões
        adicionarEventosBotoes();
    }

    // Função para adicionar os eventos de clique aos botões
    function adicionarEventosBotoes() {
        competenciaButtons.forEach(button => {
            button.addEventListener('click', () => {
                const competenciaId = button.dataset.competencia;
                mostrarDetalhes(competenciaId);
            });
        });
    }

    // Função para mostrar o personagem e esconder os detalhes (VOLTAR AO ESTADO INICIAL)
    function mostrarPersonagem() {
        personagemContainer.classList.remove('hidden');
        detalhesContainer.classList.add('hidden');
        detalhesContainer.classList.remove('flex'); // Remove 'flex' se foi adicionado
        // Remove a classe 'active' de todos os botões de competência
        competenciaButtons.forEach(btn => btn.classList.remove('active'));
    }

    // Função para mostrar os detalhes da competência
    function mostrarDetalhes(competenciaId) {
        const dados = dadosCompetencias[competenciaId];

        if (dados) {
            personagemContainer.classList.add('hidden');
            detalhesContainer.classList.remove('hidden');
            detalhesContainer.classList.add('flex'); // Garante que o layout flex seja aplicado

            tituloDetalhes.textContent = dados.titulo;
            notaDetalhes.textContent = dados.nota;
            comentariosDetalhesP.textContent = dados.comentarios;
            dicasDetalhesP.textContent = dados.dicas;

            // Atualiza o estilo do botão ativo
            competenciaButtons.forEach(btn => btn.classList.remove('active'));
            const activeButton = document.querySelector(`.competencia-btn[data-competencia="${competenciaId}"]`);
            if (activeButton) {
                activeButton.classList.add('active');
            }
        }
    }

    // Adiciona evento de clique para o botão de fechar detalhes (BOTÃO DE VOLTAR)
    if (btnFecharDetalhes) {
        btnFecharDetalhes.addEventListener('click', () => {
            mostrarPersonagem(); // Volta para a visualização do personagem
        });
    }

    // Chama a função para criar os botões quando o DOM estiver carregado
    criarBotoesCompetencia();
});