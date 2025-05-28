# STEP 8:Graph
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sms_spam_detector import y_pred,y_test,pd,svm_model,X_test_tfidf

# --- 1. Creative Confusion Matrix ---
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='coolwarm', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.title("🔥 Confusion Matrix (SVM SMS Classifier)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# --- 2. Classification Report Bar Chart ---
report = classification_report(y_test, y_pred, output_dict=True)
metrics_df = pd.DataFrame(report).transpose().iloc[:2][['precision', 'recall', 'f1-score']]
metrics_df.plot(kind='bar', figsize=(8, 5), colormap='viridis', rot=0)
plt.title("📊 Precision, Recall & F1-Score by Class")
plt.ylabel("Score")
plt.ylim(0, 1.1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(loc='lower right')
plt.show()

# --- 3. ROC Curve ---
y_scores = svm_model.decision_function(X_test_tfidf)
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.fill_between(fpr, tpr, alpha=0.3, color='orange')
plt.title('📈 ROC Curve - SVM SMS Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()

