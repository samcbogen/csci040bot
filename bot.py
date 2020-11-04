import praw
import random
import datetime
import time
from textblob import TextBlob

# FIXME:
# copy your generate_comment functions from the week_07 lab here

def generate_comment_0():
    best_synonyms = ['best', 'greatest', 'ideal', 'perfect', 'prime']
    best_word = random.choice(best_synonyms)
    him_synonyms = ['him', 'that guy', 'that dude', 'his ticket', 'this candidate']
    him_word = random.choice(him_synonyms)
    sane_synonyms = ['sane', 'clearheaded', 'rational', 'competent', 'fit for office']
    sane_word = random.choice(sane_synonyms)
    importantly_synonyms = ['importantly', 'important', 'relevant', 'cardinal', 'paramount']
    importantly_word = random.choice(importantly_synonyms)
    trump_synonyms = ['Donald Trump', 'Trump', 'Mr. Trump', 'the current president', 'a white supremacist']
    trump_word = random.choice(trump_synonyms)
    text = 'Joe Biden is the ' + best_word + ' presidential candidate -- vote for ' + him_word + '. He is bipartisan, ' + sane_word + ', and most ' + importantly_word + ', he is not ' + trump_word + '.'
    return text

def generate_comment_1():
    vote_for_synonyms = ['Vote for', 'Cast your ballot for', 'Send in your ballot that votes for', 'Elect', 'Make sure you vote for']
    vote_for_word = random.choice(vote_for_synonyms)
    biden_synonyms = ['Biden', 'Joe Biden', 'former VP Biden', 'Joesph R. Biden', 'Vice President Biden']
    biden_word = random.choice(biden_synonyms)
    americans_synonyms = ['Americans', 'people', 'folks', 'human beings', 'of us']
    americans_word = random.choice(americans_synonyms)
    listen_to_synonyms = ['listen to', 'care about', 'take action based on', 'take into account the', 'take the word of']
    listen_to_word = random.choice(listen_to_synonyms)
    trump_synonyms = ['Donald Trump', 'Trump', 'Mr. Trump', 'the current president', 'Mr. Trump']
    trump_word = random.choice(trump_synonyms)
    text = vote_for_word + ' ' + biden_word + '! He actually cares about all ' + americans_word + ', and he will actually ' + listen_to_word + ' scientists when dealing with COVID-19, unlike ' + trump_word + '!'
    return text

def generate_comment_2():
    biden_synonyms = ['Biden', 'Joe Biden', 'former VP Biden', 'Joesph R. Biden', 'Vice President Biden']
    biden_word = random.choice(biden_synonyms)
    trump_synonyms = ['Donald Trump', 'Trump', 'Mr. Trump', 'the current president', 'a white supremacist']
    trump_word = random.choice(trump_synonyms)
    president_synonyms = ['president', 'POTUS', 'President of the United States', 'the president', 'running the country']
    president_word = random.choice(president_synonyms)
    decency_synonyms = ['decency', 'character', 'dignity', 'responsibility', 'respectability']
    decency_word = random.choice(decency_synonyms)
    white_house_synonyms = ['White House', 'Oval Office', 'office of the presidency', 'United States', 'West Wing']
    white_house_word = random.choice(white_house_synonyms)
    text = 'When you vote, make sure you vote for ' + biden_word + '! He is clearly more qualified than ' + trump_word + ' to be ' + president_word + ', and he will restore ' + decency_word + ' to the ' + white_house_word + '!'
    return text

def generate_comment_3():
    trump_synonyms = ['Donald Trump', 'Trump', 'Mr. Trump', 'President Donald Trump', 'Donald J. Trump']
    trump_word = random.choice(trump_synonyms)
    awful_synonyms = ['awful', 'despicable', 'vile', 'disgusting', 'terrible']
    awful_word = random.choice(awful_synonyms)
    condemn_synonyms = ['condemn', 'criticize', 'denounce', 'deplore', 'decry']
    condemn_word = random.choice(condemn_synonyms)
    white_supremacists_synonyms = ['white supremacists', 'the proud boys', 'racists', 'white supremacy', 'racism and bigotry']
    white_supremacists_word = random.choice(white_supremacists_synonyms)
    for_office_synonyms = ['for office', 'for the office of president', 'to be president', 'to be the president', 'to run the country']
    for_office_word = random.choice(for_office_synonyms)
    text = trump_word + ' is absolutely ' + awful_word + '. He refused to ' + condemn_word + ' ' + white_supremacists_word + ', and that alone should make him unfit ' + for_office_word + '.'
    return text

def generate_comment_4():
    intro_synonyms = ['My goodness,', 'By gosh,', "Hey y'all,", 'I just wanted to let you know that', 'You should know that']
    intro_word = random.choice(intro_synonyms)
    trump_synonyms = ['Donald Trump', 'Trump', 'Mr. Trump', 'President Donald Trump', 'Donald J. Trump']
    trump_word = random.choice(trump_synonyms)
    be_reelected_syonyms = ['be re-elected', 'have your vote', 'be elected president again', 'get voted in as president again', 'earn re-election']
    be_reelected_word = random.choice(be_reelected_syonyms)
    orange_synonyms = ['orange', 'awful color of', 'ugly shade of', 'massive layer of orange', 'rust-colored']
    orange_word = random.choice(orange_synonyms)
    president_synonyms = ['president', 'POTUS', 'President of the United States', 'the president', 'running the country']
    president_word = random.choice(president_synonyms)
    text = intro_word + ' ' + trump_word + ' should not ' + be_reelected_word + '. Anyone who wears that ' + orange_word + ' makeup is clearly unfit to be ' + president_word + '.'
    return text

def generate_comment_5():
    a_declaration_synonyms = ['a declaration', 'an announcement', 'a royal decree', 'a message', 'an official announcement']
    a_declaration_word = random.choice(a_declaration_synonyms)
    this_synonyms = ['this', 'my comment', 'this comment', 'what I have to say', 'what I am writing']
    this_word = random.choice(this_synonyms)
    trump_synonyms = ['Donald Trump', 'Trump', 'Mr. Trump', 'President Donald Trump', 'Donald J. Trump']
    trump_word = random.choice(trump_synonyms)
    bad_bad_synonyms = ['bad, bad', 'mean, mean', 'cold-hearted', 'awful, awful', 'diasppointing, evil']
    bad_bad_word = random.choice(bad_bad_synonyms)
    man_synonyms = ['man', 'person', 'human', 'human being', 'child']
    man_word = random.choice(man_synonyms)
    text = 'I have ' + a_declaration_word + ' for everyone that reads ' + this_word + '! Do not vote for ' + trump_word + '! He is a ' + bad_bad_word + ' ' + man_word + ". That's all."
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    text0 = generate_comment_0()
    text1 = generate_comment_1()
    text2 = generate_comment_2()
    text3 = generate_comment_3()
    text4 = generate_comment_4()
    text5 = generate_comment_5()
    text_options = [text0, text1, text2, text3, text4, text5]
    text = random.choice(text_options)
    return text


# connect to reddit 
reddit = praw.Reddit('IzbickisArmyBot')
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jiwfn3/from_hoangs_bot_1_biden_pledges_ambitious_climate/'
submission = reddit.submission(url=reddit_debate_url)

start_time = datetime.datetime.now()

while True:
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)
    submission.comments.replace_more(limit=None)

    # FIXME (task 0): get a list of all of the comments in the submission
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)


    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    not_my_comments = []
    for comment in submission.comments.list():
        if comment.author != 'FlotsamAndBotsam':
            not_my_comments.append(comment)

    print('len(not_my_comments)=',len(not_my_comments))

    print('len(not_my_comments)=',len(not_my_comments))

    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        reply = generate_comment()
        submission.reply(reply)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        comments_without_replies = []
        for comment in not_my_comments:
            if comment.author != 'FlotsamAndBotsam':
                has_replied = False
                for reply in comment.replies:
                    if str(reply.author) == 'FlotsamAndBotsam':
                        has_replied = True
                if has_replied is False:
                    comments_without_replies.append(comment)  

        print('len(comments_without_replies)=',len(comments_without_replies))
        
        # task 4
        for comments in comments_without_replies:
            selection = random.choice(comments_without_replies)
            generated_reply = generate_comment()
            try:
                selection.reply(generated_reply)
            except praw.exceptions.RedditAPIException as error:
                if "DELETED_COMMENT" in str(error):
                    print("Comment" +  comment.id + " was deleted")
                else:
                    print("Error Found: ", error)
            except: #AssertionError
                print('found an exception ')
                print('going to sleep')
                time.sleep(60)
                print('done sleeping')

    # FIXME (task 5): select a new submission for the next iteration;
    rand = random.random()
    all_submissions = []
    if rand >= 0.5:
        print('original submission')
        submission = reddit.submission(url='https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/')
        submission.reply(generate_comment())
    if rand < 0.5:
        print('top subreddit submission')
        for submission in reddit.subreddit("csci040temp").top("day"):
            all_submissions.append(submission)
        submission_choice = random.choice(all_submissions)
        submission = reddit.submission(id=submission_choice)
        print('submission_id =',submission_choice)
        print(submission_choice.title)
   

    #downvote comments for trump
    for comment in submission.comments.list():
        if 'trump' in comment.body.lower():
            comment.downvote() 
            print('Comment Downvoted')


    #upvote comments for biden
    for comment in submission.comments.list():
        if 'biden' in comment.body.lower():
            comment.upvote()
            print('Comment Upvoted')

    
    #downvote trump submission and upvote biden submission
    if 'trump' in submission.title.lower():
        submission.downvote()
        print('Submission Upvoted')
    if 'biden' in submission.title.lower():
        submission.downvote()
        print('Submission Downvoted')

    #Upvote or downvote comments based on polarity and subjectivity:
     for comment in submission.comments.list():
        comment_blob = TextBlob(str(comment.body))
        polarity = comment_blob.sentiment.polarity
        subjectivity = comment_blob.sentiment.subjectivity
        if 'trump' in comment.body.lower() and polarity > 0.5:
            comment.upvote()
        if 'biden' in comment.body.lower() and polarity > 0.5:
            comment.downvote()
        if 'trump' in comment.body.lower() and subjectivity > 0:
            comment.upvote()
        if 'biden' in comment.body.lower() and subjectivity > 0:
            comment.downvote()
