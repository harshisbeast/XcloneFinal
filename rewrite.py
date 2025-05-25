def rewrite_commit(commit):
    if commit.author_name == b"Harsh Orkmez":
        commit.author_name = b"Harsh Singh"
        commit.author_email = b"harshsingh281272@gmail.com"
    if commit.committer_name == b"Harsh Orkmez":
        commit.committer_name = b"Harsh Singh"
        commit.committer_email = b"harshsingh281272@gmail.com"
