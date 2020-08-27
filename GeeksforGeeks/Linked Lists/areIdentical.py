def areIdentical(head1, head2):
    # Code here
    while head1!=None and head2!=None:
        if head1.data!=head2.data:
            return 0
        head1=head1.next
        head2=head2.next
    return head1==None and head2==None
