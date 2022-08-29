$( document ).ready( function ()
{
    $( '.page-home .head' ).click( function ()
    {
        if ( $( this ).parent().hasClass( 'active' ) )
        {
            $( this ).parent().removeClass( 'active' )
        } else
        {
            $( this ).parent().addClass( 'active' )
        }
    } )

    $( '.page-home .radio .input' ).click( function ()
    {
        $( '.page-home .radio .input' ).removeClass( 'checked' )
        $( '.page-home .radio .input input' ).removeAttr( 'checked' )
        $( this ).addClass( 'checked' )
        $( this ).find( 'input' ).attr( 'checked', "" )
    } )

    $( '.hamburger' ).click( function ()
    {
        var ul = $( this ).parent().find( 'ul' )
        if ( ul.hasClass( 'active' ) )
        {
            ul.removeClass( 'active' )
        } else
        {
            ul.addClass( 'active' )
        }
    } )

    $( '.page-home .switch' ).click( function ()
    {
        var input = $( this ).parent().find( 'input' )
        if ( input.is( ':checked' ) )
        {
            input.removeAttr( 'checked' )
            $( this ).removeClass( 'active' )
            $( this ).parents( '.total' ).find( '.content' ).css( 'display', 'none' )
        } else
        {
            input.attr( 'checked', "" )
            $( this ).addClass( 'active' )
            $( this ).parents( '.total' ).find( '.content' ).css( 'display', 'flex' )
        }
    } )

    $( '.popup' ).click( function ( e )
    {
        var box = e.target.querySelector( '.box' )
        if ( box )
        {
            $( this ).removeClass( 'active' )
        }
    } )
} )