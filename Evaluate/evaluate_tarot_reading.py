
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_similarity(text1, text2):
    # 中文分词
    text1_cut = " ".join(jieba.cut(text1))
    text2_cut = " ".join(jieba.cut(text2))

    # 计算 TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1_cut, text2_cut])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]

def evaluate_accuracy(answer, keywords):
    score = sum(0.2 for word in keywords if word in answer)
    return min(score, 1)  # 确保分数不超过1

def sentence_fluency(sentence):
    """
    评估单个句子的流畅性。
    """
    words = list(jieba.cut(sentence))
    num_words = len(words)
    unique_words = len(set(words))

    # 词汇多样性
    lexical_diversity = unique_words / num_words if num_words > 0 else 0

    # 合理长度判断
    if 5 <= num_words <= 30:
        length_score = 1
    else:
        length_score = 0

    # 句子流畅性
    return (lexical_diversity + length_score) / 2

def evaluate_fluency(text):
    """
    计算整体文本的流畅性。
    """
    sentences = [s.strip() for s in text.split('。') if s.strip()]  # 使用句号分割句子
    if not sentences:
        return 0

    total_fluency = sum(sentence_fluency(sentence) for sentence in sentences)
    return total_fluency / len(sentences)


def evaluate_response(question, answer, keywords):
    accuracy = evaluate_accuracy(answer, keywords)
    consistency = calculate_similarity(question, answer)
    fluency = evaluate_fluency(answer)

    # 一致性分数需要乘以0.2，以便与其他分数保持一致
    consistency_score = consistency * 0.2
    fluency = fluency * 0.2
    
    return accuracy, consistency_score, fluency

def evaluate_tarot_reading(question, keywords, answers):
    total_scores = np.zeros(3)
    for i, answer in enumerate(answers, 1):
        accuracy, consistency, fluency = evaluate_response(question, answer, keywords)
        total_scores += np.array([accuracy, consistency, fluency])
        print(f"回答 {i} - 准确性: {accuracy}, 一致性: {consistency}, 流畅性: {fluency}")


    # 计算总分
    average_scores = total_scores / len(answers)
    return average_scores

# 输入示例
question = "我在职业上会成功吗？"
keywords = ["成功", "星星牌", "希望"]
answers = [
    "星星牌表明你的成功就在眼前，预示着希望和积极性。asdas ",
    "你将在职业上取得重大成就，星星牌预示着辉煌的未来。aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "我在职业上会成功吗成功在等待你，星星牌显示出极大的希望和机遇。我在职业上会成功吗"
]

total_scores = evaluate_tarot_reading(question, keywords, answers)
print("\n总评分 - 准确性:", total_scores[0], "一致性:", total_scores[1], "流畅性:", total_scores[2])
