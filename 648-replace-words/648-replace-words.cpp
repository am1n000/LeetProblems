
class TrieNode
{
	public:
		TrieNode *child[26];
		bool  endOfWord;

		TrieNode()
		{
			this->endOfWord = false;
			for(int i = 0; i < 26; i++) this->child[i] = NULL;
		}
};

class Solution {
public:

    TrieNode *rootNode;

    void	createTrie(std::string word)
    {
        TrieNode *temp = rootNode;

        for(auto k : word)
        {
            if (!temp->child[k - 'a'])
                temp->child[k - 'a'] = new TrieNode;
            temp = temp->child[k - 'a'];
        }
        temp->endOfWord = true;
    }

    std::string get_prefix(std::string word)
    {
        TrieNode *temp = rootNode;
        std::string prefix;

        for (auto a : word)
        {
            if (temp->endOfWord == true)
                return (prefix);
            prefix += a;
            if (!temp->child[a - 'a'])
                return (word);
            temp = temp->child[a - 'a'];
        }
        return (word);
    }

    std::string replaceWords(std::vector<std::string>& dictionary, std::string sentence)
    {
        std::stringstream ss(sentence);
        std::string word;
        std::string result = "";
        rootNode = new TrieNode;

        for(auto s : dictionary)
            createTrie(s);
        for(; ss >> word;)
        {
            result += get_prefix(word);
            result += " ";
        }
        result.pop_back();

        return (result);
    }
};