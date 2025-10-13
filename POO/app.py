from typing import Any, Union


class Question:
    def __init__(self, question_text: str, correct_answer: Any) -> None:
        self.question_text = question_text
        self.correct_answer = correct_answer

    def solve(self, answer: Any) -> bool:
        return bool(self.correct_answer == answer)

    def __str__(self) -> str:
        # Para entender este método, olhe o tópico opcional na lição Herança
        return self.question_text


class MultipleChoiceQuestion(Question):
    def __init__(self, question_text: str, correct_answer: Union[int, float]) -> None:
        super().__init__(question_text, correct_answer)
        self.choices: list[str] = []

    def add_choice(self, choice: str) -> None:
        self.choices.append(choice)

    def solve(self, answer: int) -> bool:
        # Tipagem nominal dinâmica por meio da chamada à função `int`
        return super().solve(int(answer))

    def __str__(self) -> str:
        # Retorna o enunciado e todas as alternativas numeradas, separadas
        # por quebras de linha (\n)
        return (
            super().__str__()  # Retorna o enunciado
            + "\n"  # Quebra de linha entre o enunciado e alternativas
            + "\n".join(  # Junta as alternativas com quebras de linha
                f"{num} - {text}"  # Junta o número da alternativa com o texto
                # Enumera as alternativas, contando a partir do 1
                for num, text in enumerate(self.choices, start=1)
            )
        )


class TextQuestion(Question):
    def __init__(self, question_text: str, correct_answer: str) -> None:
        super().__init__(question_text, correct_answer)

    def solve(self, answer: str) -> bool:
        return super().solve(answer)


class Quiz:
    def __init__(self, questions: list[Question] = []) -> None:
        # Cria uma lista vazia se não for passada uma lista como parâmetro
        self.questions = questions

    def add_question(self, question: Question) -> None:
        self.questions.append(question)

    def solve(self) -> float:
        correct_answers = 0
        for question in self.questions:
            print(question)
            answer = input("Resposta: ")
            if question.solve(answer):
                correct_answers += 1

        return correct_answers / len(self.questions)


def create_question() -> Question:
    input_str = "Digite A para uma questão aberta e M para múltipla escolha: "
    while (question_type := input(input_str).lower()) not in ["a", "m"]:
        print("Tipo de questão inválido!")

    question_text = input("Digite o enunciado: ")

    # ? Questão aberta
    if question_type == "a":
        correct_answer = input("Digite a resposta: ")
        return TextQuestion(question_text, correct_answer)

    # ? Questão de múltipla escolha
    choices: list[str] = []
    input_str = "Digite a alternativa ou P para parar: "
    while (choice := input(input_str)).lower() != "p":
        choices.append(choice)

    input_str = "Digite o número da alternativa correta: "
    # Enquanto a pessoa digitar uma alternativa menor que 0 ou maior que a
    # última, continua perguntando
    while (correct := int(input(input_str))) < 0 or correct >= len(choices):
        print("Número de alternativa inválido!")

    question = MultipleChoiceQuestion(question_text, correct_answer=correct)

    for choice in choices:
        question.add_choice(choice)

    return question


def main() -> None:
    quiz = Quiz()

    while True:
        choice = input(
            "Digite A para adicionar uma questão, "
            "R para resolver o questionário "
            "ou S para sair: "
        ).lower()

        if choice == "a":
            quiz.add_question(create_question())
        elif choice == "r":
            result = quiz.solve() * 100
            print(f"Sua nota foi {result:.2f}%")
        elif choice == "s":
            print("Até mais!")
            break
        else:
            print("Escolha inválida!")


if __name__ == "__main__":
    while True:
        try:
            print("Vamos começar!")
            main()
        except Exception:
            pass
        else:
            break
