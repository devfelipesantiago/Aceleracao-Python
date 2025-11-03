task_form = {
    "open": '<form method="post" class="new-task">',
    "name": """<label for="nome">Atividade
            <input type="text" name="nome" id="nome" required>
        </label>""",
    "status": """<label for="status">Status
            <select name="status" id="status">
                <option value="Não iniciado">Não iniciado</option>
                <option value="Em progresso">Em progresso</option>
                <option value="Concluído">Concluído</option>
                <option value="Atrasado">Atrasado</option>
            </select>
        </label>""",
    "percentage": """<label for="percentage">Porcentagem de conclusão
            <input type="number" name="percentage" id="percentage" required>
        </label>""",
    "description": """<label for="description">Descrição da atividade
            <textarea type="text" name="description" id="description" required></textarea>
        </label>""",
    "date": """<label for="deadline">Data limite
            <input type="date" name="deadline" id="deadline" required>
        </label>""",
    "responsible": """<label for="responsible">Responsável
            <input type="text" name="responsible" id="responsible" required>
        </label>""",
    "send": '<button type="submit">Enviar</button>',
    "close": "</form>",
}

form_data = {
    "nome": "Restaurar projeto",
    "status": "Não iniciado",
    "percentage": 0,
    "description": "Restaurar projeto deletado",
    "deadline": "2023-07-15",
    "responsible": "Thiago Silva",
}
