function InterviewQuestionCard({ question, answer }) {
    return (
        <div className="interview-card">

            <h3>Interview Question</h3>

            <p className="question">
                {question}
            </p>

            {answer && (
                <div className="answer">
                    <h4>Sample Answer</h4>
                    <p>{answer}</p>
                </div>
            )}

        </div>
    );
}

export default InterviewQuestionCard;